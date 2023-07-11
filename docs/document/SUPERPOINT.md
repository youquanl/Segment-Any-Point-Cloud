<img src="../figs/logo2.png" align="right" width="26%">

# Superpixel & Superpoint
Currently, we provide superpixel generation through [SEEM](https://github.com/UX-Decoder/Segment-Everything-Everywhere-All-At-Once/tree/main), [SAM](https://github.com/facebookresearch/segment-anything) and [SLIC](https://scikit-image.org/docs/stable/api/skimage.segmentation.html#skimage.segmentation.slic). Furthermore, we offer the correspondence between superpixels and superpoints on the [nuScenes](https://www.nuscenes.org/) dataset. Coming soon, we will incorporate [X-Decoder](https://github.com/microsoft/X-Decoder), [OpenSeeD](https://github.com/IDEA-Research/OpenSeeD) and [FastSAM](https://github.com/CASIA-IVA-Lab/FastSAM) to provide support for superpixel generation.

## 1. Installation
Please follow the official [SEEM](https://github.com/UX-Decoder/Segment-Everything-Everywhere-All-At-Once/tree/main) and [SAM](https://github.com/facebookresearch/segment-anything) guidelines for installation. and other package [nuScenes devkit](https://github.com/nutonomy/nuscenes-devkit)  is **required** in order to run experiments on the [nuScenes](https://www.nuscenes.org/nuscenes) dataset.

```Shell
pip install nuscenes-devkit 
```

## 2. Superpixel generation
Superpixel generation via SEEM:
```Shell
cd generation/SEEM/demo_code
python superpixel_generation.py
```
Superpixel generation by SAM:
```Shell
cd generation/SAM
python superpixel_generation.py
```
Superpixel generation using SLIC:
```Shell
cd generation/SLIC
python superpixel_generation.py
```

Correspondence between superpixels and superpoints:
```Shell
cd generation
python superpixel2superpoint.py
```

