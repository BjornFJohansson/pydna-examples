#!/usr/bin/env bash
wget -q https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O Miniconda_latest.sh
bash Miniconda_latest.sh -b -p $HOME/miniconda
export PATH="$HOME/miniconda/bin:$PATH"
rm Miniconda_latest.sh
conda config --set always_yes yes --set show_channel_urls yes
conda update conda
conda config --add channels conda-forge
conda config --add channels BjornFJohansson
conda create -qy -n testenv python=3.7 nbval pytest lxml requests
source activate testenv
which python
python --version
conda install pydna
python run_test.py
