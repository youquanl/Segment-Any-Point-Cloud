import numpy as np
import torch
import matplotlib.pyplot as plt
import cv2
import sys
sys.path.append("..")
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator, SamPredictor
import os
import argparse
from PIL import Image
from tqdm import tqdm
from multiprocessing import Pool
from nuscenes.nuscenes import NuScenes


def compute_sam(cam_token, sp_root):
    cam = nusc.get("sample_data", cam_token)
    image = cv2.imread(os.path.join(nusc.dataroot, cam["filename"]))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    masks = mask_generator.generate(image)

    sorted_anns = sorted(masks, key=(lambda x: x['area']), reverse=True)
    segments_sam = np.zeros((image.shape[0], image.shape[1]))
    for id, ann in enumerate(sorted_anns):
        m = ann['segmentation']
        segments_sam[m] = id

    im = Image.fromarray(segments_sam.astype(np.uint8))
    im.save(
        sp_root + cam["token"] + ".png"
    )


def parse_option():
    parser = argparse.ArgumentParser('SAM', add_help=False)
    parser.add_argument('-r', '--root_folder', help='root folder of dataset',
                        default='./data_root/nuScenes')
    parser.add_argument('-s', '--sp_folder', help='superpixels root', type=str,
                        default='./superpixels/nuscenes/superpixels_sam/') 
    parser.add_argument('-p', '--sam_checkpoint', help='path of pretrained model', type=str,
                        default='./sam_vit_h_4b8939.pth')
    args = parser.parse_args()

    return args



if __name__ == "__main__":
    args = parse_option()
    sam_checkpoint = args.sam_checkpoint
    model_type = "vit_h"
    device = "cuda"
    sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
    sam.to(device=device)
    mask_generator = SamAutomaticMaskGenerator(sam)


    nuscenes_path = args.root_folder
    assert os.path.exists(nuscenes_path), f"nuScenes not found in {nuscenes_path}"

    nusc = NuScenes(
        version="v1.0-trainval", dataroot=nuscenes_path, verbose=False
    )
    os.makedirs(args.sp_folder)

    camera_list = [
        "CAM_FRONT",
        "CAM_FRONT_RIGHT",
        "CAM_BACK_RIGHT",
        "CAM_BACK",
        "CAM_BACK_LEFT",
        "CAM_FRONT_LEFT",
    ]

    for scene_idx in tqdm(range(len(nusc.scene))):
        scene = nusc.scene[scene_idx]
        current_sample_token = scene["first_sample_token"]
        while current_sample_token != "":
            current_sample = nusc.get("sample", current_sample_token)
            for camera_name in camera_list:
               compute_sam(current_sample["data"][camera_name], args.sp_folder )

            current_sample_token = current_sample["next"]








