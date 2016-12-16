#!/usr/bin/env bash 
wget -q https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O Miniconda_latest.sh
bash Miniconda_latest.sh -b -p $HOME/miniconda
export PATH="$HOME/miniconda/bin:$PATH"
rm Miniconda_latest.sh
conda update -yq conda
conda config --add channels BjornFJohansson
conda create -q -y -n testenv python=3.5 pydna nbval pytest lxml requests
source activate testenv
which python
python --version
python run_test.py
