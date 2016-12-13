wget -q https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O Miniconda_latest.sh
bash Miniconda_latest.sh -b -p $HOME/miniconda
export PATH="$HOME/miniconda/bin:$PATH"
rm Miniconda_latest.sh
conda update -yq conda
conda config --add channels BjornFJohansson
conda env create -f test_environment.yml -q
source activate testenv
which python
python --version
python run_test.py
