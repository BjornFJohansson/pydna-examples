#!/usr/bin/env bash

wget -q https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O Miniconda_latest.sh
bash Miniconda_latest.sh -b -p $HOME/miniconda
export PATH="$HOME/miniconda/bin:$PATH"
rm Miniconda_latest.sh


conda config --set always_yes yes --set show_channel_urls yes
conda update conda
conda env create -f environment.yml
source activate testenvironment
conda config --add channels conda-forge
conda install pytest nbconvert nbval termcolor


# This is to make sure double stars ** works
shopt -s globstar

# This script runs, tests and converts (to html) all Jupyter notebooks in /notebooks
# Probably running and converting should be turned off when the notebooks are ready for publication
# notebooks with names starting with a dot . or in a folder starting with a dot are ignored.

cd notebooks

# command to run all notebooks
#jupyter nbconvert --ExecutePreprocessor.kernel_name=python3 --execute --inplace --allow-errors **/*.ipynb

#command to convert all notebooks
#jupyter nbconvert **/*.ipynb

#command to test all notebooks
pytest --current-env --capture=no --nbval **/*.ipynb



exit $?
