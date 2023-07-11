<img src="../figs/logo2.png" align="right" width="26%">

# Superpixel & Superpoint

```
└── generation
      │── SLIC
      │── SAM
      │── OpenSeeD
      │── X-Decoder
      │── SEEM
      │── FastSAM
      └── Semantic-SAM
```

## Update
- \[2023.07\] - We provide the code for generating semantic superpixels through [SLIC](https://scikit-image.org/docs/stable/api/skimage.segmentation.html#skimage.segmentation.slic), [SAM](https://github.com/facebookresearch/segment-anything), and [SEEM](https://github.com/UX-Decoder/Segment-Everything-Everywhere-All-At-Once). Meanwhile, we include the code for building correspondence between semantic superpixels and semantic superpoints on the [nuScenes](https://www.nuscenes.org/) dataset. Our next update aims to integrate more VFMs, such as [OpenSeeD](https://github.com/IDEA-Research/OpenSeeD), [X-Decoder](https://github.com/microsoft/X-Decoder), and [FastSAM](https://github.com/CASIA-IVA-Lab/FastSAM).

## 1. Installation
- Kindly follow the official guideline of [SAM](https://github.com/facebookresearch/segment-anything) and [SEEM](https://github.com/UX-Decoder/Segment-Everything-Everywhere-All-At-Once) for the installation details. 

- Note that [nuScenes devkit](https://github.com/nutonomy/nuscenes-devkit)  is **required** in order to generate semantic superpixels on the [nuScenes](https://www.nuscenes.org/nuscenes) dataset.

  ```Shell
  pip install nuscenes-devkit 
  ```

## 2. Semantic Superpixel Generation

- Semantic superpixel generation using [SLIC](https://scikit-image.org/docs/stable/api/skimage.segmentation.html#skimage.segmentation.slic):
  ```Shell
  cd generation/SLIC
  python superpixel_generation.py
  ```

- Semantic superpixel generation using [SAM](https://github.com/facebookresearch/segment-anything):
  ```Shell
  cd generation/SAM
  python superpixel_generation.py
  ```

- Semantic superpixel generation using [SEEM](https://github.com/UX-Decoder/Segment-Everything-Everywhere-All-At-Once):
  ```Shell
  cd generation/SEEM/demo_code
  python superpixel_generation.py
  ```


## 3. Building Correspondence

- The following code builds the 2D-3D correspondence between the semantic superpixel and semantic superpoint:
  ```Shell
  cd generation
  python superpixel2superpoint.py
  ```

