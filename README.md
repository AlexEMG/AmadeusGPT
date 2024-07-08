<div align="center">
  
<p align="center">
<img src="https://images.squarespace-cdn.com/content/v1/57f6d51c9f74566f55ecf271/8555eac6-6af0-4538-bda4-c1a8a2c7bed8/amadeusgpt_logo.png?format=1500w" width="95%">
</p>

[![Downloads](https://pepy.tech/badge/amadeusgpt)](https://pepy.tech/project/amadeusgpt)
[![Downloads](https://pepy.tech/badge/amadeusgpt/month)](https://pepy.tech/project/amadeusgpt)
[![PyPI version](https://badge.fury.io/py/amadeusgpt.svg)](https://badge.fury.io/py/amadeusgpt)
[![GitHub stars](https://img.shields.io/github/stars/AdaptiveMotorControlLab/AmadeusGPT.svg?style=social&label=Star)](https://github.com/AdaptiveMotorControlLab/AmadeusGPT)

## 🪄  We turn natural language descriptions of behaviors into machine-executable code.

[🛠️ Installation](https://github.com/AdaptiveMotorControlLab/AmadeusGPT?tab=readme-ov-file#install--run-amadeusgpt) |
[🌎 Home Page](http://www.mackenziemathislab.org/amadeusgpt) |
[🚨 News](https://github.com/AdaptiveMotorControlLab/AmadeusGPT?tab=readme-ov-file#news) |
[🪲 Reporting Issues](https://github.com/AdaptiveMotorControlLab/AmadeusGPT/issues) |
[💬 Discussions!](https://github.com/AdaptiveMotorControlLab/AmadeusGPT/discussions)

</div>

- We use large language models (LLMs) to bridge natural language and behavior analysis.
- This work is published at **NeurIPS2023!** Read the paper, [AmadeusGPT: a natural language interface for interactive animal behavioral analysis]([https://www.google.com/search?q=amadeusgpt+openreview&sca_esv=590699485&rlz=1C5CHFA_enCH1059CH1060&ei=K1N6ZaHdKvmrur8PosOOkAo&ved=0ahUKEwjhnta83I2DAxX5le4BHaKhA6IQ4dUDCBE&uact=5&oq=amadeusgpt+openreview&gs_lp=Egxnd3Mtd2l6LXNlcnAiFWFtYWRldXNncHQgb3BlbnJldmlldzIHECEYoAEYCjIHECEYoAEYCki2HVDfAliOHHACeACQAQGYAYMDoAHaGaoBCDEuMTEuMS40uAEDyAEA-AEBwgIFECEYqwLCAggQABiABBiiBMICCBAAGIkFGKIE4gMEGAEgQYgGAQ&sclient=gws-wiz-serp#:~:text=AmadeusGPT%3A%20a%20natural,net%20%E2%80%BA%20pdf](https://proceedings.neurips.cc/paper_files/paper/2023/file/1456560769bbc38e4f8c5055048ea712-Paper-Conference.pdf)) by [Shaokai Ye](https://github.com/yeshaokai), [Jessy Lauer](https://github.com/jeylau), [Mu Zhou](https://github.com/zhoumu53), [Alexander Mathis](https://github.com/AlexEMG) & [Mackenzie W. Mathis](https://github.com/MMathisLab).
- Like this project? Please consider giving us a star ⭐️!
  
## Install & Run AmadeusGPT🎻

### Install with `pypi`

- AmadeusGPT is a Python package hosted on `pypi`. You can create a virtual env (conda, etc, see below*) and run:
```python
pip install 'amadeusgpt[streamlit]'
```
Note that in order to access our demo video and keypoint files, we recommend to install from the source.

### Install from the source

#### Minimal installation
**Recommended for:** Running AmadeusGPT without GPUs. This setup is lightweight and is limited to processing movie files and keypoint outputs (.h5) from DeepLabCut.

```bash
# Install the minimal environment
bash install_minimal.sh

# Activate the conda environment
conda activate amadeusgpt-minimal
```

#### GPU installation
**Recommended for:** Users on Linux with GPUs. Support for Windows and MacOS will be added in the future.

```bash
# Install the gpu environment
bash install_gpu.sh

# Activate the conda environment
conda activate amadeusgpt-gpu
```

#### CPU installation
**Recommended for:** MacOS / Linux users working with very small video files.

```bash
# Install the cpu environment
bash install_cpu.sh

# Activate the conda environment
conda activate amadeusgpt-cpu
```


### Setup OpenAI API Key to use AmadeusGPT

**Why OpenAI API Key is needed** AmadeusGPT relies on API calls of OpenAI (we will add more options in the future) for language understanding and code writing.

You can either add this into your environment by following:

```bash
export OPENAI_API_KEY='your API key' 
```

Or inside your python script or jupyter notebook, add this line in the beginning of the file


```python
import os
os.environ["OPENAI_API_KEY"] = 'your api key' 
```

- Please note that you need an [openAI API key](https://platform.openai.com/account/api-keys), which you can easily create [here](https://platform.openai.com/account/api-keys).



### Try AmadeusGPT with local web app
```python
make app
```

### What keypoint file format do we support?
- If you only provide the raw video file, we use SuperAnimal models [SuperAnimal models] (https://www.nature.com/articles/s41467-024-48792-2) to predict your video. This is only supported with cpu or gpu installation. While we highly recommend gpu installation, we are working on faster, light-weight superanimal models to work on your CPU.
- If you already have keypoint file corresponding to the video file, look up how we set-up the config file in the notebooks.  Right now we only support keypoint output from DeepLabCut. Other keypoint formats can be added upon feature requests.


### Try AmadeusGPT with our example notebooks
We provide example notebooks at [Notebooks](notebook)

### Notebook as use-case demo

1) Draw ROI and ask when is the animal in the ROI.  [Demo](notebook/EPM_demo.ipynb)
2) Obtain the binary mask for retrieved masks (for further sampling such as neural data pairing) [Demo](notebook/EPM_demo.ipynb)
3) Use SuperAnimal video inference (make sure you use gpu or cpu installation) if you don't have corresponding DeepLabCut keypoint file [Demo](notebook/custom_mouse_demo.ipynb)
4) Write you own integration modules and use them [Demo](notebook/Horse_demo.ipynb) [Source code](amadeusgpt/integration_modules). Make sure you delete the cached modules_embedding.pickle if you add new modules
5) Multi-Animal social interaction.  [Demo](notebook/MABe_demo.ipynb)
6) Reuse the task program generated by LLM and run it on different videos [Demo](notebook/MABe_demo.ipynb)

## Citation

  If you use ideas or code from this project in your work, please cite us  using the following BibTeX entry. 🙏

```
@article{ye2023amadeusGPT,
      title={AmadeusGPT: a natural language interface for interactive animal behavioral analysis}, 
      author={Shaokai Ye and Jessy Lauer and Mu Zhou and Alexander Mathis and Mackenzie Weygandt Mathis},
      journal={Thirty-seventh Conference on Neural Information Processing Systems},
      year={2023},
      url={https://openreview.net/forum?id=9AcG3Tsyoq},
```
- arXiv preprint version **[AmadeusGPT: a natural language interface for interactive animal behavioral analysis](https://arxiv.org/abs/2307.04858)** by [Shaokai Ye](https://github.com/yeshaokai), [Jessy Lauer](https://github.com/jeylau), [Mu Zhou](https://github.com/zhoumu53), [Alexander Mathis](https://github.com/AlexEMG) & [Mackenzie W. Mathis](https://github.com/MMathisLab).


## License 

AmadeusGPT is license under the Apache-2.0 license.
  -  🚨 Please note several key dependencies have their own licensing. Please carefully check the license information for [DeepLabCut](https://github.com/DeepLabCut/DeepLabCut) (LGPL-3.0 license), [SAM](https://github.com/facebookresearch/segment-anything) (Apache-2.0 license), [CEBRA](https://github.com/AdaptiveMotorControlLab/CEBRA) (Non-Commercial), etc.


## News
- 🤩 Dec 2023, code released!
- 🔥 Our work was accepted to NeuRIPS2023
- 🧙‍♀️ Open-source code coming in the fall of 2023
- 🔮 arXiv paper and demo released July 2023
- 🪄[Contact us](http://www.mackenziemathislab.org/)
