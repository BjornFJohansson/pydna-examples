#!/usr/bin/env bash
wget -q https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O Miniconda_latest.sh
bash Miniconda_latest.sh -b -p $HOME/miniconda
export PATH="$HOME/miniconda/bin:$PATH"
rm Miniconda_latest.sh

conda config --set always_yes yes --set show_channel_urls yes
conda update conda
conda config --add channels BjornFJohansson
conda create -qy -n testenv python=3.6 nbval pytest lxml requests
source activate testenv
which python
python --version

conda install pydna
#conda install -c BjornFJohansson/label/test pydna=2.0.0a3

python run_test.py
