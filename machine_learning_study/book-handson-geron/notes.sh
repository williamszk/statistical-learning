# Create a virtual environment for this dir theme
python3 -m venv .venv

source .venv/bin/activate

pip3 install jupyter jupyterlab pandas scikit-learn
pip3 install jupyterlab==3.6.0a4
pip3 install jupyterlab-vim

# to start the jupyter notebook
# jupyter notebook --ip 0.0.0.0 --allow-root --port 3000 --no-browser
jupyter lab --ip 0.0.0.0 --allow-root --port 3000 --no-browser
# https://github.com/jwkvam/jupyterlab-vim

hello hello
