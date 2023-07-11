# --------------------------------------------------------
# SEEM -- Segment Everything Everywhere All At Once
# Copyright (c) 2022 Microsoft
# Licensed under The MIT License [see LICENSE for details]
# Written by Xueyan Zou (xueyan@cs.wisc.edu), Jianwei Yang (jianwyan@microsoft.com)
# --------------------------------------------------------

import os
import warnings
import PIL
from PIL import Image
from typing import TYPE_CHECKING, Any, Callable, Dict, List, Optional, Tuple
import cv2
import torch
import argparse
import numpy as np
from nuscenes.nuscenes import NuScenes
from xdecoder.BaseModel import BaseModel
from xdecoder import build_model
from utils.distributed import init_distributed
from utils.arguments import load_opt_from_config_files
from utils.constants import COCO_PANOPTIC_CLASSES
from tqdm import tqdm
from tasks import *

def compute_seem(cam_token):
    cam = nusc.get("sample_data", cam_token)
    image = Image.open(os.path.join(nusc.dataroot, cam["filename"]))
    image = {'image':image, 'mask':None}
    with torch.autocast(device_type='cuda', dtype=torch.float16):
        interactive_infer_image(model,  image, task, sp_path=args.sp_folder  + cam["token"] + ".png")


def parse_option():
    parser = argparse.ArgumentParser('SEEM', add_help=False)
    parser.add_argument('--conf_files', default="configs/seem/seem_focall_lang.yaml", metavar="FILE", help='path to config file', )
    parser.add_argument('-r', '--root_folder', help='root folder of dataset',
                        default='./data/sets/nuscenes')
    parser.add_argument('-s', '--sp_folder', help='superpixels root', type=str,
                        default='./superpixels/nuscenes/superpixels_seem/') 
    parser.add_argument('-p', '--pretrained_pth', help='path of pretrained model', type=str,
                        default='./seem_focall_v1.pt')
    args = parser.parse_args()

    return args



if __name__ == "__main__":
    '''
    build args
    '''
    args = parse_option()
    opt = load_opt_from_config_files(args.conf_files)
    opt = init_distributed(opt)

    # META DATA
    cur_model = 'None'
    if 'focalt' in args.conf_files:
        pretrained_pth = args.pretrained_pth
        if not os.path.exists(pretrained_pth):
            os.system("wget {}".format("https://huggingface.co/xdecoder/SEEM/resolve/main/seem_focalt_v2.pt"))
        cur_model = 'Focal-T'
    elif 'focal' in args.conf_files:
        pretrained_pth = args.pretrained_pth
        if not os.path.exists(pretrained_pth):
            os.system("wget {}".format("https://huggingface.co/xdecoder/SEEM/resolve/main/seem_focall_v1.pt"))
        cur_model = 'Focal-L'

    '''
    build model
    '''
    model = BaseModel(opt, build_model(opt)).from_pretrained(pretrained_pth).eval().cuda()
    with torch.no_grad():
        model.model.sem_seg_head.predictor.lang_encoder.get_text_embeddings(COCO_PANOPTIC_CLASSES + ["background"], is_eval=True)

    task = ['Panoptic']

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
               compute_seem(current_sample["data"][camera_name])

            current_sample_token = current_sample["next"]








