import os
import numpy as np
import copy
from PIL import Image
from pyquaternion import Quaternion
from nuscenes.nuscenes import NuScenes
from nuscenes.utils.geometry_utils import view_points
from nuscenes.utils.splits import create_splits_scenes
from nuscenes.utils.data_classes import LidarPointCloud
import json
import argparse
import random
from pathlib import Path
from tqdm import tqdm
import pickle
seed = 1242
random.seed(seed)
np.random.seed(seed)



def map_pointcloud_to_image(data, sp_root, min_dist: float = 1.0):
    """
    Given a lidar token and camera sample_data token, load pointcloud and map it to
    the image plane. Code adapted from nuscenes-devkit
    https://github.com/nutonomy/nuscenes-devkit.
    :param min_dist: Distance from the camera below which points are discarded.
    """
    pointsensor = nusc.get("sample_data", data["LIDAR_TOP"])
    pcl_path = os.path.join(nusc.dataroot, pointsensor["filename"])
    pc_original = LidarPointCloud.from_file(pcl_path)
    pc_ref = pc_original.points

    camera_list = [
        "CAM_FRONT",
        "CAM_FRONT_RIGHT",
        "CAM_BACK_RIGHT",
        "CAM_BACK",
        "CAM_BACK_LEFT",
        "CAM_FRONT_LEFT",
    ]
    label_set = np.ones((len(pc_ref.T)),dtype=np.int32) * -1  # (m,)
    label = 0  
    for i, camera_name in enumerate(camera_list):
        pc = copy.deepcopy(pc_original)
        cam = nusc.get("sample_data", data[camera_name])
        im = np.array(Image.open(os.path.join(nusc.dataroot, cam["filename"])))
        sp = Image.open(
             sp_root +"/" + cam["token"] + ".png"
        )
        sp = np.array(sp)

        # Points live in the point sensor frame. So they need to be transformed via
        # global to the image plane.
        # First step: transform the pointcloud to the ego vehicle frame for the
        # timestamp of the sweep.
        cs_record = nusc.get(
            "calibrated_sensor", pointsensor["calibrated_sensor_token"]
        )
        pc.rotate(Quaternion(cs_record["rotation"]).rotation_matrix)
        pc.translate(np.array(cs_record["translation"]))

        # Second step: transform from ego to the global frame.
        poserecord = nusc.get("ego_pose", pointsensor["ego_pose_token"])
        pc.rotate(Quaternion(poserecord["rotation"]).rotation_matrix)
        pc.translate(np.array(poserecord["translation"]))

        # Third step: transform from global into the ego vehicle frame for the
        # timestamp of the image.
        poserecord = nusc.get("ego_pose", cam["ego_pose_token"])
        pc.translate(-np.array(poserecord["translation"]))
        pc.rotate(Quaternion(poserecord["rotation"]).rotation_matrix.T)

        # Fourth step: transform from ego into the camera.
        cs_record = nusc.get(
            "calibrated_sensor", cam["calibrated_sensor_token"]
        )
        pc.translate(-np.array(cs_record["translation"]))
        pc.rotate(Quaternion(cs_record["rotation"]).rotation_matrix.T)

        # Fifth step: actually take a "picture" of the point cloud.
        # Grab the depths (camera frame z axis points away from the camera).
        depths = pc.points[2, :]

        # Take the actual picture
        # (matrix multiplication with camera-matrix + renormalization).
        points = view_points(
            pc.points[:3, :],
            np.array(cs_record["camera_intrinsic"]),
            normalize=True,
        )

        # Remove points that are either outside or behind the camera.
        # Also make sure points are at least 1m in front of the camera to avoid
        # seeing the lidar points on the camera
        # casing for non-keyframes which are slightly out of sync.
        points = points[:2].T
        mask = np.ones(depths.shape[0], dtype=bool)
        mask = np.logical_and(mask, depths > min_dist)
        mask = np.logical_and(mask, points[:, 0] > 0)
        mask = np.logical_and(mask, points[:, 0] < im.shape[1] - 1)
        mask = np.logical_and(mask, points[:, 1] > 0)
        mask = np.logical_and(mask, points[:, 1] < im.shape[0] - 1)
        matching_points = np.where(mask)[0]
        matching_pixels = np.round(
            np.flip(points[matching_points], axis=1)
        ).astype(np.int64)

        sp_value = sp[matching_pixels[:, 0], matching_pixels[:, 1]]  # (m_match,)
        inds, counts = np.unique(sp_value, return_counts=True)
        top = inds[np.argsort(-counts)][: ]   
            
        # for ii in top:
        #     mask_org_len =  np.zeros(mask.shape[0], dtype=bool) 
        #     mask2 = np.in1d(sp_value, ii)
        #     if np.sum(mask2) < 40:
        #         continue
        #     else:    
        #         mask_org_len[mask] = mask2
        #         mask3 = np.zeros(mask_org_len.shape[0], dtype=bool) 
        #         mask3[mask_org_len] = label_set[mask_org_len] == -1 
        #         mask_org_len1 = np.logical_and(mask3, mask_org_len)
                
        #         if len(label_set[mask_org_len1]) < 40:
        #             continue
        #         else:
        #             mask4 = np.zeros(mask_org_len.shape[0], dtype=bool) 
        #             Range = np.sqrt(pc_ref.T[mask_org_len1][:, 0] ** 2 + pc_ref.T[mask_org_len1][:, 1] ** 2 + pc_ref.T[mask_org_len1][:,2] ** 2)
        #             mean_xyz = np.mean(Range)
        #             mask_r = Range - mean_xyz < 8
        #             mask4[mask_org_len1] = mask_r
            
        #             label_set[mask4] = label
        #             label += 1
        for ii in top:
            mask_org_len =  np.zeros(mask.shape[0], dtype=bool) 
            mask2 = np.in1d(sp_value, ii)
            mask_org_len[mask] = mask2
            label_set[mask_org_len] = label
            label += 1


    assert len(pc_ref.T) == len(label_set)
    return pc_ref.T, label_set.reshape(-1,1)


def create_list_of_tokens(scene):
    # Get first in the scene
    current_sample_token = scene["first_sample_token"]

    # Loop to get all successive keyframes
    while current_sample_token != "":
        current_sample = nusc.get("sample", current_sample_token)
        next_sample_token = current_sample["next"]
        list_tokens.append(current_sample["data"])
        current_sample_token = next_sample_token



def parse_arguments():

    parser = argparse.ArgumentParser(description='superpixel2superpoint')
    parser.add_argument('-r', '--root_folder', help='root folder of dataset',
                        default='./data/sets/nuscenes')
    parser.add_argument('-s', '--sp_folder', help='superpixels root', type=str,
                        default='./superpixels/nuscenes/superpixels_seem')  
    arguments = parser.parse_args()

    return arguments



if __name__ == "__main__":
    args = parse_arguments()
    nusc = NuScenes(
        version="v1.0-trainval", dataroot=args.root_folder, verbose=False)
    phase_scenes = create_splits_scenes()['train']
    skip_counter = 0
    skip_ratio = 1
    list_tokens = []
    for scene_idx in tqdm(range(len(nusc.scene))):
        scene = nusc.scene[scene_idx]
        if scene["name"] in phase_scenes:
            skip_counter += 1
            if skip_counter % skip_ratio == 0:
                create_list_of_tokens(scene)
    
    for idx in range(len(list_tokens)):
        lidar_token = list_tokens[idx]
        pc, labels = map_pointcloud_to_image(lidar_token, args.sp_folder)