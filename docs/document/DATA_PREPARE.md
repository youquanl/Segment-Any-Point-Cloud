<img src="../figs/logo2.png" align="right" width="26%">

# Data Preparation

### Overview

| [**nuScenes**](https://www.nuscenes.org/nuscenes) | [**SemanticKITTI**](http://semantic-kitti.org/) | [**Waymo Open**](https://waymo.com/open) | [**ScribbleKITTI**](https://github.com/ouenal/scribblekitti) |
| :-: | :-: | :-: | :-: |
| <img width="115" src="../figs/dataset/nuscenes.png"> | <img width="125" src="../figs/dataset/semantickitti.png"> | <img width="125" src="../figs/dataset/waymo-open.png"> | <img width="125" src="../figs/dataset/scribblekitti.png"> | 
| [**RELLIS-3D**](http://www.unmannedlab.org/research/RELLIS-3D) | [**SemanticPOSS**](http://www.poss.pku.edu.cn/semanticposs.html) | [**SemanticSTF**](https://github.com/xiaoaoran/SemanticSTF) | [**DAPS-3D**](https://github.com/subake/DAPS3D) |
| <img width="125" src="../figs/dataset/rellis-3d.png"> | <img width="125" src="../figs/dataset/semanticposs.png"> | <img width="125" src="../figs/dataset/semanticstf.png"> | <img width="125" src="../figs/dataset/daps-3d.png"> | 
| [**SynLiDAR**](https://github.com/xiaoaoran/SynLiDAR) | [**Synth4D**](https://github.com/saltoricristiano/gipso-sfouda) | [**nuScenes-C**](https://github.com/ldkong1205/Robo3D) |
| <img width="125" src="../figs/dataset/synlidar.png"> | <img width="125" src="../figs/dataset/synth4d.png"> | <img width="125" src="../figs/dataset/nuscenes-c.png"> |

### Overall Structure

```
└── data 
    └── sets
        │── nuscenes
        │── semantickitti
        │── scribblekitti
        │── waymo_open
        │── rellis3d
        │── semanticposs
        │── semanticstf
        │── daps3d       
        │── synlidar
        │── syn4d
        └── nuscenes_c
```

## nuScenes

To install the [nuScenes-lidarseg](https://www.nuscenes.org/nuscenes) dataset, download the data, annotations, and other files from https://www.nuscenes.org/download.

Unpack the compressed file(s) into `/data/sets/nuscenes` and your folder structure should end up looking like this:

```
└── nuscenes  
    ├── Usual nuscenes folders (i.e. samples, sweep)
    │
    ├── lidarseg
    │   └── v1.0-{mini, test, trainval} <- contains the .bin files; a .bin file 
    │                                      contains the labels of the points in a 
    │                                      point cloud (note that v1.0-test does not 
    │                                      have any .bin files associated with it)
    │
    └── v1.0-{mini, test, trainval}
        ├── Usual files (e.g. attribute.json, calibrated_sensor.json etc.)
        ├── lidarseg.json  <- contains the mapping of each .bin file to the token   
        └── category.json  <- contains the categories of the labels (note that the 
                              category.json from nuScenes v1.0 is overwritten)
```

Please note that you should cite the corresponding paper(s) once you use the dataset.

```bibtex
@article{fong2022panopticnuscenes,
    author = {Whye Kit Fong and Rohit Mohan and Juana Valeria Hurtado and Lubing Zhou and Holger Caesar and Oscar Beijbom and Abhinav Valada},
    title = {Panoptic nuScenes: A Large-Scale Benchmark for LiDAR Panoptic Segmentation and Tracking},
    journal = {IEEE Robotics and Automation Letters},
    volume = {7},
    number = {2},
    pages = {3795--3802},
    year = {2022}
}
```
```bibtex
@inproceedings{caesar2020nuscenes,
    author = {Holger Caesar and Varun Bankiti and Alex H Lang and Sourabh Vora and Venice Erin Liong and Qiang Xu and Anush Krishnan and Yu Pan and Giancarlo Baldan and Oscar Beijbom},
    title = {nuScenes: A Multimodal Dataset for Autonomous Driving},
    booktitle = {IEEE/CVF Conference on Computer Vision and Pattern Recognition},
    pages = {11621--11631},
    year = {2020}
}
```


## SemanticKITTI

To install the [SemanticKITTI](http://semantic-kitti.org/index) dataset, download the data, annotations, and other files from http://semantic-kitti.org/dataset.

Unpack the compressed file(s) into `/data/sets/semantickitti` and re-organize the data structure. Your folder structure should end up looking like this:

```
└── semantickitti  
    └── sequences
        ├── velodyne <- contains the .bin files; a .bin file contains the points in a point cloud
        │    └── 00
        │    └── ···
        │    └── 21
        ├── labels   <- contains the .label files; a .label file contains the labels of the points in a point cloud
        │    └── 00
        │    └── ···
        │    └── 10
        ├── calib
        │    └── 00
        │    └── ···
        │    └── 21
        └── semantic-kitti.yaml
```

Please note that you should cite the corresponding paper(s) once you use the dataset.


```bibtex
@inproceedings{behley2019semantickitti,
    author = {Jens Behley and Martin Garbade and Andres Milioto and Jan Quenzel and Sven Behnke and Jürgen Gall and Cyrill Stachniss},
    title = {SemanticKITTI: A Dataset for Semantic Scene Understanding of LiDAR Sequences},
    booktitle = {IEEE/CVF International Conference on Computer Vision},
    pages = {9297--9307},
    year = {2019}
}
```
```bibtex
@inproceedings{geiger2012kitti,
    author = {Andreas Geiger and Philip Lenz and Raquel Urtasun},
    title = {Are We Ready for Autonomous Driving? The KITTI Vision Benchmark Suite},
    booktitle = {IEEE/CVF Conference on Computer Vision and Pattern Recognition},
    pages = {3354--3361},
    year = {2012}
}
```


## ScribbleKITTI

To install the [ScribbleKITTI](https://arxiv.org/abs/2203.08537) dataset, download the annotations from https://data.vision.ee.ethz.ch/ouenal/scribblekitti.zip. Note that you only need to download these annotation files (~118.2MB); the data is the same as [SemanticKITTI](http://semantic-kitti.org/index).

Unpack the compressed file(s) into `/data/sets/scribblekitti` and re-organize the data structure. Your folder structure should end up looking like this:


```
└── scribblekitti 
    └── sequences
        └── scribbles <- contains the .label files; a .label file contains the scribble labels of the points in a point cloud
             └── 00
             └── ···
             └── 10
```

Please note that you should cite the corresponding paper(s) once you use the dataset.

```bibtex
@inproceedings{unal2022scribble,
    author = {Ozan Unal and Dengxin Dai and Luc Van Gool},
    title = {Scribble-Supervised LiDAR Semantic Segmentation},
    booktitle = {IEEE/CVF Conference on Computer Vision and Pattern Recognition},
    pages = {2697--2707},
    year = {2022}
}
```


## Waymo Open

Coming soon.

Please note that you should cite the corresponding paper(s) once you use the dataset.

```bibtex
@inproceedings{sun2020waymoopen,
    author = {Pei Sun and Henrik Kretzschmar and Xerxes Dotiwalla and Aurelien Chouard and Vijaysai Patnaik and Paul Tsui and James Guo and Yin Zhou and Yuning Chai and Benjamin Caine and Vijay Vasudevan and Wei Han and Jiquan Ngiam and Hang Zhao and Aleksei Timofeev and Scott Ettinger and Maxim Krivokon and Amy Gao and Aditya Joshi and Yu Zhang and Jonathon Shlens and Zhifeng Chen and Dragomir Anguelov},
    title = {Scalability in Perception for Autonomous Driving: Waymo Open Dataset},
    booktitle = {IEEE/CVF Conference on Computer Vision and Pattern Recognition},
    pages = {2446--2454},
    year = {2020}
}
```


## RELLIS-3D

Coming soon.

Please note that you should cite the corresponding paper(s) once you use the dataset.

```bibtex
@inproceedings{jiang2021rellis3d,
    author = {Peng Jiang and Philip Osteen and Maggie Wigness and Srikanth Saripallig},
    title = {RELLIS-3D Dataset: Data, Benchmarks and Analysis},
    booktitle = {IEEE International Conference on Robotics and Automation},
    pages = {1110--1116},
    year = {2021}
}
```


## SemanticPOSS

Coming soon.

Please note that you should cite the corresponding paper(s) once you use the dataset.

```bibtex
@inproceedings{pan2020semanticposs,
    author = {Yancheng Pan and Biao Gao and Jilin Mei and Sibo Geng and Chengkun Li and Huijing Zhao},
    title = {SemanticPOSS: A Point Cloud Dataset with Large Quantity of Dynamic Instances},
    booktitle = {IEEE Intelligent Vehicles Symposium},
    pages = {687--693},
    year = {2020}
}
```


## SemanticSTF

Coming soon.

Please note that you should cite the corresponding paper(s) once you use the dataset.

```bibtex
@inproceedings{bijelic2020stf,
    author = {Mario Bijelic and Tobias Gruber and Fahim Mannan and Florian Kraus and Werner Ritter and Klaus Dietmayer and Felix Heide},
    title = {Seeing through Fog without Seeing Fog: Deep Multimodal Sensor Fusion in Unseen Adverse Weather},
    booktitle = {IEEE/CVF Conference on Computer Vision and Pattern Recognition},
    pages = {11682--11692},
    year = {2020}
}
```
```bibtex
@inproceedings{xiao2023semanticstf,
    author = {Aoran Xiao and Jiaxing Huang and Weihao Xuan and Ruijie Ren and Kangcheng Liu and Dayan Guan and Abdulmotaleb El Saddik and Shijian Lu and Eric Xing},
    title = {3D Semantic Segmentation in the Wild: Learning Generalized Models for Adverse-Condition Point Clouds},
    booktitle = {IEEE/CVF Conference on Computer Vision and Pattern Recognition},
    pages = {9382--9392},
    year = {2023}
}
```


## DAPS-3D

Coming soon.

Please note that you should cite the corresponding paper(s) once you use the dataset.

```bibtex
@article{klokov2023daps3d,
    author = {Alexey Klokov and Di Un Pak and Aleksandr Khorin and Dmitry Yudin and Leon Kochiev and Vladimir Luchinskiy and Vitaly Bezuglyj},
    title = {DAPS3D: Domain Adaptive Projective Segmentation of 3D LiDAR Point Clouds},
    journal = {Preprint},
    year = {2023}
}
```


## SynLiDAR

Coming soon.

Please note that you should cite the corresponding paper(s) once you use the dataset.

```bibtex
@inproceedings{xiao2022synlidar,
    author = {Aoran Xiao and Jiaxing Huang and Dayan Guan and Fangneng Zhan and Shijian Lu},
    title = {Transfer Learning from Synthetic to Real LiDAR Point Cloud for Semantic Segmentation},
    booktitle = {AAAI Conference on Artificial Intelligence},
    pages = {2795--2803},
    year = {2022}
}
```


## Synth4D

Coming soon.

Please note that you should cite the corresponding paper(s) once you use the dataset.

```bibtex
@inproceedings{saltori2020synth4d,
    author = {Cristiano Saltori and Evgeny Krivosheev and Stéphane Lathuiliére and Nicu Sebe and Fabio Galasso and Giuseppe Fiameni and Elisa Ricci and Fabio Poiesi},
    title = {GIPSO: Geometrically Informed Propagation for Online Adaptation in 3D LiDAR Segmentation},
    booktitle = {European Conference on Computer Vision},
    pages = {567--585},
    year = {2022}
}
```


## nuScenes-C

Coming soon.

Please note that you should cite the corresponding paper(s) once you use the dataset.

```bibtex
@article{kong2023robo3D,
    author = {Lingdong Kong and Youquan Liu and Xin Li and Runnan Chen and Wenwei Zhang and Jiawei Ren and Liang Pan and Kai Chen and Ziwei Liu},
    title = {Robo3D: Towards Robust and Reliable 3D Perception against Corruptions},
    journal = {arXiv preprint arXiv:2303.17597},
    year = {2023}
}
```

