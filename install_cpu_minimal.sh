#!/bin/bash
source /Users/shaokaiye/miniforge3/bin/activate
conda env create -f conda/amadesuGPT-minimal.yml
conda activate amadeusgpt-minimal

pip install -e .[streamlit]
