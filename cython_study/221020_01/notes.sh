# https://cython.readthedocs.io/en/latest/src/quickstart/install.html

apt install build-essential python3-dev

# https://phoenixnap.com/kb/upgrade-python

apt install python3.9
python3.9 --version

update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1
update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 2

# root@d03aa4273aef:~/statistical-learning/cython_study# python3 --version
# Python 3.9.5

update-alternatives --config python3
# There are 2 choices for the alternative python3 (providing /usr/bin/python3).

#   Selection    Path                Priority   Status
# ------------------------------------------------------------
# * 0            /usr/bin/python3.9   2         auto mode
#   1            /usr/bin/python3.8   1         manual mode
#   2            /usr/bin/python3.9   2         manual mode

apt install python3.9-venv

python3 -m venv .venv

pip install Cython

# https://cython.readthedocs.io/en/latest/src/quickstart/build.html
touch filename.pyx
cythonize -i filename.pyx

apt install python3-dev
apt install python3.9-dev

python setup.py build_ext --inplace

# https://cython.readthedocs.io/en/latest/src/quickstart/cythonize.html




