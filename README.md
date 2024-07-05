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
- This work is published at **NeurIPS2023!** Read the paper, [AmadeusGPT: a natural language interface for interactive animal behavioral analysis](https://www.google.com/search?q=amadeusgpt+openreview&sca_esv=590699485&rlz=1C5CHFA_enCH1059CH1060&ei=K1N6ZaHdKvmrur8PosOOkAo&ved=0ahUKEwjhnta83I2DAxX5le4BHaKhA6IQ4dUDCBE&uact=5&oq=amadeusgpt+openreview&gs_lp=Egxnd3Mtd2l6LXNlcnAiFWFtYWRldXNncHQgb3BlbnJldmlldzIHECEYoAEYCjIHECEYoAEYCki2HVDfAliOHHACeACQAQGYAYMDoAHaGaoBCDEuMTEuMS40uAEDyAEA-AEBwgIFECEYqwLCAggQABiABBiiBMICCBAAGIkFGKIE4gMEGAEgQYgGAQ&sclient=gws-wiz-serp#:~:text=AmadeusGPT%3A%20a%20natural,net%20%E2%80%BA%20pdf) by [Shaokai Ye](https://github.com/yeshaokai), [Jessy Lauer](https://github.com/jeylau), [Mu Zhou](https://github.com/zhoumu53), [Alexander Mathis](https://github.com/AlexEMG) & [Mackenzie W. Mathis](https://github.com/MMathisLab).
- Like this project? Please consider giving us a star ⭐️!
  
## Install & Run AmadeusGPT🎻

### Install with `pypi`

- AmadeusGPT is a Python package hosted on `pypi`. You can create a virtual env (conda, etc, see below*) and run:
```python
pip install 'amadeusgpt[streamlit]'
```
Note that in order to access our demo video and keypoint files, you will need to clone the repo.

### Install from the source

We have prepared 3 bash installation scripts.  Make sure you edit the path of conda / forge to your in the installation scripts.

```bash
# Recommended if you are running AmadeusGPT without gpus. The installation is light-weight and you can only use it with movie files and keypoint output (.h5) from DeepLabCut.
bash install_minimal.sh

conda activate amadeusgpt-minimal
```   

```bash
# Recommended if you are running on linux with gpus (We will add Windows and MacsOS support in the future).
bash install_gpu.sh

conda activate amadeusgpt-gpu
```

```bash
#For MacOS users, if you are only playing with very small video files.
bash install_cpu.sh

conda activate amadeusgpt-cpu
```
### Setup OpenAI Key to use AmadeusGPT

 - Please note that you need an [openAI API key](https://platform.openai.com/account/api-keys), which you can easily create [here](https://platform.openai.com/account/api-keys).
- If you want the **Streamlit Demo on your computer**, you will also need demo files that are supplied in our repo (see below**), so please git clone the repo and navigate into the `AmadeusGPT` directory. Then in your conda env/terminal run  `pip install 'amadeusgpt[streamlit]'` as described above. Then, to launch the Demo App execute in the terminal:

### Try AmadeusGPT with local web app
```python
make app
```

### Try AmadeusGPT with our example notebooks
We provide example notebooks at [Notebooks](notebook)

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
