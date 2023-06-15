<img src="../figs/logo2.png" align="right" width="26%">

# Installation

### General Requirements

This codebase is tested with `torch==1.10.0` and `torchvision==0.11.2`, with `CUDA 11.3`. In order to successfully reproduce the results reported in our paper, we recommend you to follow the exact same configuation with us. However, similar versions that came out lately should be good as well.


### Step 1: Create Enviroment
```Shell
conda create -n seal python=3.9.15
```

### Step 2: Activate Enviroment
```Shell
conda activate seal
```

### Step 3: Install PyTorch
```Shell
conda install pytorch==1.10.0 torchvision==0.11.2 cudatoolkit=11.3 -c pytorch
```

### Step 4: Install Necessary Libraries
#### 4.1 - [nuScenes devkit](https://github.com/nutonomy/nuscenes-devkit)
> **Note:** This toolkit is **required** in order to run experiments on the [nuScenes](https://www.nuscenes.org/nuscenes) dataset.
```Shell
pip install nuscenes-devkit 
```

#### 4.2 - [PyTorch Scatter](https://github.com/rusty1s/pytorch_scatter)
```Shell
conda install pytorch-scatter -c pyg
```

#### 4.3 - [MinkowskiEngine](https://github.com/NVIDIA/MinkowskiEngine)
```Shell
pip install MinkowskiEngine == 0.5.4
```

#### 4.4 - [PyTorch Lightnin](https://github.com/Lightning-AI/lightning)
```Shell
pip install pytorch_lightning == 1.4.0
```

#### 4.5 - [SparseConv](https://github.com/traveller59/spconv)
```Shell
pip install spconv == 2.3.6
```

### Step 5: Install Other Packages
```Shell
pip install pyyaml easydict numba
```

## Enviroment Summary

We provide the list of all packages and their corresponding versions installed in this codebase:
```Shell
#
# Name                    Version                   Build  Channel
_libgcc_mutex             0.1                        main  
_openmp_mutex             5.1                       1_gnu  
absl-py                   1.3.0                    pypi_0    pypi
addict                    2.4.0                    pypi_0    pypi
aiohttp                   3.8.4                    pypi_0    pypi
aiosignal                 1.3.1                    pypi_0    pypi
anyio                     3.6.2                    pypi_0    pypi
argon2-cffi               21.3.0                   pypi_0    pypi
argon2-cffi-bindings      21.2.0                   pypi_0    pypi
asttokens                 2.2.0                    pypi_0    pypi
async-timeout             4.0.2                    pypi_0    pypi
attrs                     22.1.0                   pypi_0    pypi
backcall                  0.2.0                    pypi_0    pypi
beautifulsoup4            4.11.1                   pypi_0    pypi
blas                      1.0                         mkl  
bleach                    5.0.1                    pypi_0    pypi
bzip2                     1.0.8                h7f98852_4    conda-forge
ca-certificates           2023.01.10           h06a4308_0    anaconda
cachetools                5.2.0                    pypi_0    pypi
ccimport                  0.4.2                    pypi_0    pypi
certifi                   2023.5.7         py39h06a4308_0  
cffi                      1.15.1                   pypi_0    pypi
charset-normalizer        2.1.1                    pypi_0    pypi
contourpy                 1.0.6                    pypi_0    pypi
cudatoolkit               11.3.1              h9edb442_10    conda-forge
cumm-cu113                0.4.9                    pypi_0    pypi
cycler                    0.11.0                   pypi_0    pypi
cython                    0.29.32                  pypi_0    pypi
debugpy                   1.6.4                    pypi_0    pypi
decorator                 5.1.1                    pypi_0    pypi
defusedxml                0.7.1                    pypi_0    pypi
descartes                 1.1.0                    pypi_0    pypi
easydict                  1.10                     pypi_0    pypi
entrypoints               0.4                      pypi_0    pypi
executing                 1.2.0                    pypi_0    pypi
fastjsonschema            2.16.2                   pypi_0    pypi
ffmpeg                    4.3                  hf484d3e_0    pytorch
fire                      0.4.0                    pypi_0    pypi
fonttools                 4.38.0                   pypi_0    pypi
freetype                  2.10.4               h0708190_1    conda-forge
frozenlist                1.3.3                    pypi_0    pypi
fsspec                    2023.5.0                 pypi_0    pypi
future                    0.18.3                   pypi_0    pypi
gmp                       6.2.1                h58526e2_0    conda-forge
gnutls                    3.6.13               h85f3911_1    conda-forge
google-auth               2.14.1                   pypi_0    pypi
google-auth-oauthlib      0.4.6                    pypi_0    pypi
grpcio                    1.51.1                   pypi_0    pypi
h5py                      3.7.0                    pypi_0    pypi
idna                      3.4                      pypi_0    pypi
imageio                   2.9.0                    pypi_0    pypi
importlib-metadata        5.1.0                    pypi_0    pypi
intel-openmp              2021.4.0          h06a4308_3561  
ipykernel                 6.17.1                   pypi_0    pypi
ipython                   8.7.0                    pypi_0    pypi
ipython-genutils          0.2.0                    pypi_0    pypi
ipywidgets                8.0.2                    pypi_0    pypi
jbig                      2.1               h7f98852_2003    conda-forge
jedi                      0.18.2                   pypi_0    pypi
jinja2                    3.1.2                    pypi_0    pypi
joblib                    1.2.0                    pypi_0    pypi
jpeg                      9e                   h166bdaf_1    conda-forge
jsonschema                4.17.3                   pypi_0    pypi
jupyter                   1.0.0                    pypi_0    pypi
jupyter-client            7.4.7                    pypi_0    pypi
jupyter-console           6.4.4                    pypi_0    pypi
jupyter-core              5.1.0                    pypi_0    pypi
jupyter-server            1.23.3                   pypi_0    pypi
jupyterlab-pygments       0.2.2                    pypi_0    pypi
jupyterlab-widgets        3.0.3                    pypi_0    pypi
kiwisolver                1.4.4                    pypi_0    pypi
lame                      3.100             h7f98852_1001    conda-forge
lark                      1.1.5                    pypi_0    pypi
lcms2                     2.12                 hddcbb42_0    conda-forge
ld_impl_linux-64          2.38                 h1181459_1  
lerc                      2.2.1                h9c3ff4c_0    conda-forge
libdeflate                1.7                  h7f98852_5    conda-forge
libffi                    3.4.2                h6a678d5_6  
libgcc-ng                 11.2.0               h1234567_1  
libgfortran-ng            8.2.0                hdf63c60_1    anaconda
libgomp                   11.2.0               h1234567_1  
libiconv                  1.17                 h166bdaf_0    conda-forge
libopenblas               0.3.2                h9ac9557_1    anaconda
libpng                    1.6.37               h21135ba_2    conda-forge
libstdcxx-ng              11.2.0               h1234567_1  
libtiff                   4.3.0                hf544144_1    conda-forge
libuv                     1.43.0               h7f98852_0    conda-forge
libwebp-base              1.2.2                h7f98852_1    conda-forge
llvmlite                  0.39.1                   pypi_0    pypi
loguru                    0.6.0                    pypi_0    pypi
lz4-c                     1.9.3                h9c3ff4c_1    conda-forge
markdown                  3.4.1                    pypi_0    pypi
markupsafe                2.1.1                    pypi_0    pypi
matplotlib                3.6.2                    pypi_0    pypi
matplotlib-inline         0.1.6                    pypi_0    pypi
minkowskiengine           0.5.4                    pypi_0    pypi
mistune                   2.0.4                    pypi_0    pypi
mkl                       2021.4.0           h06a4308_640  
mkl-service               2.4.0            py39h7e14d7c_0    conda-forge
mkl_fft                   1.3.1            py39h0c7bc48_1    conda-forge
mkl_random                1.2.2            py39hde0f152_0    conda-forge
mmcv-full                 1.2.7                    pypi_0    pypi
msgpack                   1.0.4                    pypi_0    pypi
msgpack-numpy             0.4.8                    pypi_0    pypi
multidict                 6.0.4                    pypi_0    pypi
multimethod               1.9                      pypi_0    pypi
nbclassic                 0.4.8                    pypi_0    pypi
nbclient                  0.7.2                    pypi_0    pypi
nbconvert                 7.2.5                    pypi_0    pypi
nbformat                  5.7.0                    pypi_0    pypi
ncurses                   6.3                  h5eee18b_3  
nest-asyncio              1.5.6                    pypi_0    pypi
nettle                    3.6                  he412f7d_0    conda-forge
networkx                  3.1                      pypi_0    pypi
ninja                     1.11.1                   pypi_0    pypi
notebook                  6.5.2                    pypi_0    pypi
notebook-shim             0.2.2                    pypi_0    pypi
numba                     0.56.4                   pypi_0    pypi
numpy                     1.23.4           py39h14f4228_0  
numpy-base                1.23.4           py39h31eccc5_0  
nuscenes-devkit           1.1.9                    pypi_0    pypi
oauthlib                  3.2.2                    pypi_0    pypi
olefile                   0.46               pyh9f0ad1d_1    conda-forge
openblas-devel            0.3.2                         0    anaconda
opencv-python             4.6.0.66                 pypi_0    pypi
openh264                  2.1.1                h780b84a_0    conda-forge
openjpeg                  2.4.0                hb52868f_1    conda-forge
openssl                   1.1.1t               h7f8727e_0  
packaging                 21.3                     pypi_0    pypi
pandocfilters             1.5.0                    pypi_0    pypi
parso                     0.8.3                    pypi_0    pypi
pccm                      0.4.7                    pypi_0    pypi
pexpect                   4.8.0                    pypi_0    pypi
pickleshare               0.7.5                    pypi_0    pypi
pillow                    8.3.1                    pypi_0    pypi
pip                       22.2.2           py39h06a4308_0  
platformdirs              2.5.4                    pypi_0    pypi
plyfile                   0.9                      pypi_0    pypi
portalocker               2.7.0                    pypi_0    pypi
prettytable               3.5.0                    pypi_0    pypi
prometheus-client         0.15.0                   pypi_0    pypi
prompt-toolkit            3.0.33                   pypi_0    pypi
protobuf                  3.20.3                   pypi_0    pypi
psutil                    5.9.4                    pypi_0    pypi
ptyprocess                0.7.0                    pypi_0    pypi
pure-eval                 0.2.2                    pypi_0    pypi
pyasn1                    0.4.8                    pypi_0    pypi
pyasn1-modules            0.2.8                    pypi_0    pypi
pybind11                  2.10.4                   pypi_0    pypi
pycocotools               2.0.6                    pypi_0    pypi
pycparser                 2.21                     pypi_0    pypi
pydeprecate               0.3.1                    pypi_0    pypi
pygments                  2.13.0                   pypi_0    pypi
pyparsing                 3.0.9                    pypi_0    pypi
pyquaternion              0.9.9                    pypi_0    pypi
pyrsistent                0.19.2                   pypi_0    pypi
python                    3.9.15               h7a1cb2a_2  
python-dateutil           2.8.2                    pypi_0    pypi
python_abi                3.9                      2_cp39    conda-forge
pytorch                   1.10.1          py3.9_cuda11.3_cudnn8.2.0_0    pytorch
pytorch-lightning         1.4.0                    pypi_0    pypi
pytorch-mutex             1.0                        cuda    pytorch
pytorch-scatter           2.0.9           py39_torch_1.10.0_cu113    pyg
pywavelets                1.4.1                    pypi_0    pypi
pyyaml                    6.0                      pypi_0    pypi
pyzmq                     24.0.1                   pypi_0    pypi
qtconsole                 5.4.0                    pypi_0    pypi
qtpy                      2.3.0                    pypi_0    pypi
readline                  8.2                  h5eee18b_0  
requests                  2.28.1                   pypi_0    pypi
requests-oauthlib         1.3.1                    pypi_0    pypi
rsa                       4.9                      pypi_0    pypi
scikit-image              0.18.2                   pypi_0    pypi
scikit-learn              1.1.3                    pypi_0    pypi
scipy                     1.9.3                    pypi_0    pypi
send2trash                1.8.0                    pypi_0    pypi
setuptools                59.5.0                   pypi_0    pypi
shapely                   1.8.5.post1              pypi_0    pypi
sharedarray               3.2.2                    pypi_0    pypi
six                       1.16.0             pyh6c4a22f_0    conda-forge
sniffio                   1.3.0                    pypi_0    pypi
soupsieve                 2.3.2.post1              pypi_0    pypi
spconv-cu113              2.3.6                    pypi_0    pypi
sqlite                    3.40.0               h5082296_0  
stack-data                0.6.2                    pypi_0    pypi
strictyaml                1.6.2                    pypi_0    pypi
tabulate                  0.9.0                    pypi_0    pypi
tensorboard               2.11.0                   pypi_0    pypi
tensorboard-data-server   0.6.1                    pypi_0    pypi
tensorboard-plugin-wit    1.8.1                    pypi_0    pypi
tensorpack                0.11                     pypi_0    pypi
termcolor                 2.1.1                    pypi_0    pypi
terminado                 0.17.0                   pypi_0    pypi
threadpoolctl             3.1.0                    pypi_0    pypi
tifffile                  2023.4.12                pypi_0    pypi
tinycss2                  1.2.1                    pypi_0    pypi
tk                        8.6.12               h1ccaba5_0  
toml                      0.10.2                   pypi_0    pypi
torchmetrics              0.4.0                    pypi_0    pypi
torchpack                 0.3.1                    pypi_0    pypi
torchsparse               1.4.0                    pypi_0    pypi
torchvision               0.11.2               py39_cu113    pytorch
tornado                   6.2                      pypi_0    pypi
tqdm                      4.64.1                   pypi_0    pypi
traitlets                 5.6.0                    pypi_0    pypi
typing_extensions         4.4.0              pyha770c72_0    conda-forge
tzdata                    2022f                h04d1e81_0  
urllib3                   1.26.13                  pypi_0    pypi
wcwidth                   0.2.5                    pypi_0    pypi
webencodings              0.5.1                    pypi_0    pypi
websocket-client          1.4.2                    pypi_0    pypi
werkzeug                  2.2.2                    pypi_0    pypi
wheel                     0.37.1             pyhd3eb1b0_0  
widgetsnbextension        4.0.3                    pypi_0    pypi
xz                        5.2.6                h5eee18b_0  
yapf                      0.32.0                   pypi_0    pypi
yarl                      1.9.2                    pypi_0    pypi
zipp                      3.11.0                   pypi_0    pypi
zlib                      1.2.13               h5eee18b_0  
zstd                      1.5.0                ha95c52a_0    conda-forge
```

