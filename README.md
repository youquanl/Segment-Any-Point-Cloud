<p align="right">English | <a href="./README_CN.md">简体中文</a></p>

<p align="center">
  <img src="docs/figs/logo.png" align="center" width="44%">
  
  <h3 align="center"><strong>Segment Any Point Cloud Sequences by Distilling Vision Foundation Models</strong></h3>

  <p align="center">
    <a href="https://github.com/youquanl">Youquan Liu</a><sup>1,*</sup>&nbsp;
    <a href="https://ldkong.com">Lingdong Kong</a><sup>1,2,*</sup>&nbsp;
    <a href="http://cen-jun.com">Jun Cen</a><sup>3</sup>&nbsp;
    <a href="https://scholar.google.com/citations?user=Uq2DuzkAAAAJ">Runnan Chen</a><sup>4</sup>&nbsp;
    <a href="http://zhangwenwei.cn">Wenwei Zhang</a><sup>1,5</sup>&nbsp;
    <a href="https://scholar.google.com/citations?user=lSDISOcAAAAJ">Liang Pan</a><sup>5</sup>&nbsp;
    <a href="http://chenkai.site">Kai Chen</a><sup>1</sup>&nbsp;
    <a href="https://liuziwei7.github.io">Ziwei Liu</a><sup>5</sup>&nbsp;
    <br>
    <sup>1</sup>Shanghai AI Laboratory&nbsp;&nbsp;&nbsp;
    <sup>2</sup>NUS&nbsp;&nbsp;&nbsp;
    <sup>3</sup>HKUST&nbsp;&nbsp;&nbsp;
    <sup>4</sup>HKU&nbsp;&nbsp;&nbsp;
    <sup>5</sup>S-Lab, NTU
  </p>

</p>

<p align="center">
  <a href="" target='_blank'>
    <img src="https://img.shields.io/badge/Paper-%F0%9F%93%83-purple">
  </a>
  
  <a href="https://ldkong.com/Seal" target='_blank'>
    <img src="https://img.shields.io/badge/Project-%F0%9F%94%97-violet">
  </a>
  
  <a href="" target='_blank'>
    <img src="https://img.shields.io/badge/Demo-%F0%9F%8E%AC-purple">
  </a>
  
  <a href="" target='_blank'>
    <img src="https://img.shields.io/badge/%E4%B8%AD%E8%AF%91%E7%89%88-%F0%9F%90%BC-violet">
  </a>
  
  <a href="" target='_blank'>
    <img src="https://visitor-badge.laobi.icu/badge?page_id=ldkong1205.LaserMix&left_color=gray&right_color=purple">
  </a>
</p>


# Seal :seal:
**Seal** is a versatile self-supervised learning framework capable of segmenting *any* automotive point clouds by leveraging off-the-shelf knowledge from vision foundation models (VFMs) and encouraging spatial and temporal consistency from such knowledge during the representation learning stage.

<p align="center">
  <img src="docs/figs/teaser.jpg" align="center" width="95%">
</p>

### :sparkles: Highlight
- :rocket: **Scalability:** Seal directly distills the knowledge from VFMs into point clouds, eliminating the need for annotations in either 2D or 3D during pretraining.
- :balance_scale: **Consistency:** Seal enforces the spatial and temporal relationships at both the camera-to-LiDAR and point-to-segment stages, facilitating cross-modal representation learning.
- :rainbow: **Generalizability:** Seal enables knowledge transfer in an off-the-shelf manner to downstream tasks involving diverse point clouds, including those from real/synthetic, low/high-resolution, large/small-scale, and clean/corrupted datasets.

### :oncoming_automobile: 2D-3D Correspondence
<p align="center">
  <img src="docs/figs/demo.gif" align="center" width="95%">
</p>


### :movie_camera: Video Demo
| Demo 1 | Demo 2| Demo 3|
| :-: | :-: | :-: |
| <img width="100%" src="docs/figs/demo1.jpg"> | <img width="100%" src="docs/figs/demo2.jpg"> | <img width="100%" src="docs/figs/demo3.jpg"> | 
| [Link]() <sup>:arrow_heading_up:</sup> | [Link]() <sup>:arrow_heading_up:</sup> | [Link]() <sup>:arrow_heading_up:</sup> |


## Updates
- \[2023.06\] - Our paper is available on arXiv, click [here]() to check it out. Code will be available later!


## Outline
- [Installation](#installation)
- [Data Preparation](#data-preparation)
- [Getting Started](#getting-started)
- [Main Result](#main-result)
- [TODO List](#todo-list)
- [License](#license)
- [Acknowledgement](#acknowledgement)
- [Citation](#citation)


## Installation
Please refer to [INSTALL.md](docs/INSTALL.md) for the installation details.


## Data Preparation
We verify the effectiveness of **Seal :seal:** on **eleven** different point cloud datasets, including those consisting of `real-world`, `synthetic`, `low-resolution`, `high-resolution`, `small-scale`, `large-scale`, `clean`, and `corrupted` point clouds.

| [**nuScenes**](https://www.nuscenes.org/nuscenes) | [**SemanticKITTI**](http://semantic-kitti.org/) | [**Waymo Open**](https://waymo.com/open) | [**ScribbleKITTI**](https://github.com/ouenal/scribblekitti) |
| :-: | :-: | :-: | :-: |
| <img width="115" src="docs/figs/dataset/nuscenes.png"> | <img width="115" src="docs/figs/dataset/semantickitti.png"> | <img width="115" src="docs/figs/dataset/waymo-open.png"> | <img width="115" src="docs/figs/dataset/scribblekitti.png"> | 
| [**RELLIS-3D**](http://www.unmannedlab.org/research/RELLIS-3D) | [**SemanticPOSS**](http://www.poss.pku.edu.cn/semanticposs.html) | [**SemanticSTF**](https://github.com/xiaoaoran/SemanticSTF) | [**DAPS-3D**](https://github.com/subake/DAPS3D) |
| <img width="115" src="docs/figs/dataset/rellis-3d.png"> | <img width="115" src="docs/figs/dataset/semanticposs.png"> | <img width="115" src="docs/figs/dataset/semanticstf.png"> | <img width="115" src="docs/figs/dataset/daps-3d.png"> | 
| [**SynLiDAR**](https://github.com/xiaoaoran/SynLiDAR) | [**Synth4D**](https://github.com/saltoricristiano/gipso-sfouda) | [**nuScenes-C**](https://github.com/ldkong1205/Robo3D) |
| <img width="115" src="docs/figs/dataset/synlidar.png"> | <img width="115" src="docs/figs/dataset/synth4d.png"> | <img width="115" src="docs/figs/dataset/nuscenes-c.png"> |

Please refer to [DATA_PREPARE.md](docs/DATA_PREPARE.md) for the details to prepare these datasets.


## Superpoint Generation

| Raw Point Cloud | Semantic Superpoint | Groundtruth |
| :-: | :-: | :-: |
| <img src="docs/figs/rotate/rotate1.gif" align="center" width="240"> | <img src="docs/figs/rotate/rotate1_sp.gif" align="center" width="240"> | <img src="docs/figs/rotate/rotate1_gt.gif" align="center" width="240"> | 
| |
| <img src="docs/figs/rotate/rotate2.gif" align="center" width="240"> | <img src="docs/figs/rotate/rotate2_sp.gif" align="center" width="240"> | <img src="docs/figs/rotate/rotate2_gt.gif" align="center" width="240"> |
| |
| <img src="docs/figs/rotate/rotate3.gif" align="center" width="240"> | <img src="docs/figs/rotate/rotate3_sp.gif" align="center" width="240"> | <img src="docs/figs/rotate/rotate3_gt.gif" align="center" width="240"> |
| |
| <img src="docs/figs/rotate/rotate4.gif" align="center" width="240"> | <img src="docs/figs/rotate/rotate4_sp.gif" align="center" width="240"> | <img src="docs/figs/rotate/rotate4_gt.gif" align="center" width="240"> |

Kindly refer to [SUPERPOINT.md](docs/SUPERPOINT.md) for the details to generate the semantic superpixels & superpoints with vision foundation models.


## Getting Started
Kindly refer to [GET_STARTED.md](docs/GET_STARTED.md) to learn more usage about this codebase.


## Main Result

### :unicorn: Framework Overview

| <img src="docs/figs/framework.jpg" align="center" width="99%"> |
| :-: |
| Overview of the **Seal :seal:** framework. We generate, for each {LiDAR, camera} pair at timestamp t and another LiDAR frame at timestamp t + n, the semantic superpixel and superpoint by VFMs. Two pertaining objectives are then formed, including *spatial contrastive learning* between paired LiDAR and cameras features and *temporal consistency regularization* between segments at different timestamps. |

### :car: Cosine Similaristy

| <img src="docs/figs/cosine.jpg" align="center" width="99%"> |
| :-: |
| The *cosine similarity* between a query point (red dot) and the feature learned with SLIC and different VFMs in our **Seal :seal:** framework. The queried semantic classes from top to bottom examples are: “car”, “manmade”, and “truck”. The color goes from violet to yellow denoting low and high similarity scores, respectively. |

### :blue_car: Linear Probing

| <img src="docs/figs/linear.gif" align="center" width="99%"> |
| :-: |
| The qualitative results of our **Seal :seal:** framework pretrained on nuScenes (without using groundtruth labels) and linear probed with a frozen backbone and a linear classification head. To highlight the differences, the correct / incorrect predictions are painted in gray / red, respectively. |

### :bus: Downstream Task

| <img src="docs/figs/qualitative.jpg" align="center" width="99%"> |
| :-: |
| The qualitative results of **Seal :seal:** and prior methods pretrained on nuScenes (without using groundtruth labels) and fine-tuned with 1% labeled data. To highlight the differences, the correct / incorrect predictions are painted in gray / red, respectively. |


## TODO List

- [x] Initial release. :rocket:
- [x] Add license. See [here](#license) for more details.
- [x] Add video demos :movie_camera:
- [ ] Add installation details.
- [ ] Add data preparation details.
- [ ] Add evaluation details.
- [ ] Add training details.


## Citation

If you find this work helpful, please kindly consider citing our paper:

```bibtex
@article{liu2023segment,
  title = {Segment Any Point Cloud Sequences by Distilling Vision Foundation Models},
  author = {Liu, Youquan and Kong, Lingdong and Cen, Jun and Chen, Runnan and Zhang, Wenwei and Pan, Liang and Chen, Kai and Liu, Ziwei},
  journal = {arXiv preprint arXiv:23xx.xxxxx}, 
  year = {2023},
}
```

```bibtex
@misc{liu2023segment_any_point_cloud,
  title = {The Segment Any Point Cloud Codebase},
  author = {Liu, Youquan and Kong, Lingdong and Cen, Jun and Chen, Runnan and Zhang, Wenwei and Pan, Liang and Chen, Kai and Liu, Ziwei},
  howpublished = {\url{https://github.com/youquanl/Segment-Any-Point-Cloud}},
  year = {2023},
}
```

## License
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/80x15.png" /></a>
<br />
This work is under the <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.


## Acknowledgement
This work is developed based on the [MMDetection3D](https://github.com/open-mmlab/mmdetection3d) codebase.

><img src="https://github.com/open-mmlab/mmdetection3d/blob/main/resources/mmdet3d-logo.png" width="30%"/><br>
> MMDetection3D is an open source object detection toolbox based on PyTorch, towards the next-generation platform for general 3D detection. It is a part of the OpenMMLab project developed by MMLab.

Part of this codebase has been adapted from [SLidR](https://github.com/valeoai/SLidR), [Segment Anything](https://github.com/facebookresearch/segment-anything), [X-Decoder](https://github.com/microsoft/X-Decoder), [OpenSeeD](https://github.com/IDEA-Research/OpenSeeD), [Segment Everything Everywhere All at Once](https://github.com/UX-Decoder/Segment-Everything-Everywhere-All-At-Once), [LaserMix](https://github.com/ldkong1205/LaserMix), and [Robo3D](https://github.com/ldkong1205/Robo3D).

:heart: We thank the exceptional contributions from the above open-source repositories!
