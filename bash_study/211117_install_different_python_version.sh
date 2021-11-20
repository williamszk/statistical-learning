# The objective of this exercise is to install a different python version
# than what is installed in a computer.
# e.g. in a computer there is python 3.6.9 (or any other version) as the default
# I want to install a binary that is 3.9.8, but do not overwrite
# the default python version

# connect to the EC2 instance for a test
ssh -i "C:\Users\william.suzuki\Documents\study\aws_study\aws_personal_ubuntu_server_key.pem" ubuntu@ec2-18-229-156-231.sa-east-1.compute.amazonaws.com

python3 --version
# Python 3.8.10

# we want to install python 3.9.8
# but without overwritting the default python version

# sites to find the interested version of python
# https://www.python.org/downloads/
# https://www.python.org/downloads/release/python-398/
# https://www.python.org/ftp/python/3.9.8/Python-3.9.8.tgz


# source: https://stackoverflow.com/a/46258340/8782077
# 1) Install Required Packages for source compilation
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install build-essential checkinstall
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

# 2) Download and extract desired Python version
wget https://www.python.org/ftp/python/3.9.8/Python-3.9.8.tgz
# wget https://www.python.org/ftp/python/3.9.8/Python-3.9.8.tgz --no-check-certificate
tar zxvf Python-3.9.8.tgz
rm -rf Python-3.9.8.tgz

# 3) Compile and Install Python Source
cd Python-3.9.8
sudo ./configure
sudo make altinstall

# after all the steps above are complete you can see the followign:
# ubuntu@ip-172-31-2-39:~/Documents/Python-3.9.8$ ls
# CODE_OF_CONDUCT.md  Grammar  LICENSE  Mac       Makefile.pre     Misc     Objects  PCbuild  Programs  README.rst  aclocal.m4  config.guess  config.status  configure     install-sh      netlify.toml    pyconfig.h     python         python-config.py  setup.py    
# Doc                 Include  Lib      Makefile  Makefile.pre.in  Modules  PC       Parser   Python    Tools       build       config.log    config.sub     configure.ac  libpython3.9.a  pybuilddir.txt  pyconfig.h.in  python-config  python-gdb.py

# we are interested in the binary called python (with lower case p)
# we can write ./python to start python 3.9.8

# ubuntu@ip-172-31-2-39:~/Documents/Python-3.9.8$ ./python
# Python 3.9.8 (main, Nov 17 2021, 20:10:30)
# [GCC 9.3.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>>

cd

# create a virtual environment with venv for python 3.9.8
/home/ubuntu/Documents/Python-3.9.8/python -m venv venv
# /home/william/Documents/Python-3.9.8/python -m venv venv

source venv/bin/activate
python3

# (venv) ubuntu@ip-172-31-2-39:~$ python3
# Python 3.9.8 (main, Nov 17 2021, 20:10:30)
# [GCC 9.3.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>>


# we can see that we are using the python 3.9.8

# see if inside the virtual enviroment using python3 --version and whereis python3
# we get python 3.9.8

# (inside the virtual environmnet)
python3 --version

# (venv) ubuntu@ip-172-31-2-39:~$ python3 --version
# Python 3.9.8

whereis python3
# python3: /usr/bin/python3 /usr/bin/python3.8 /usr/lib/python3 /usr/lib/python3.8 
# /usr/lib/python3.9 /etc/python3 /etc/python3.8 /usr/local/bin/python3.9 /usr/local/bin/python3.9-config 
# /usr/local/lib/python3.8 /usr/local/lib/python3.9 /usr/share/python3 /home/ubuntu/venv/bin/python3 
# /home/ubuntu/venv/bin/python3.9 /usr/share/man/man1/python3.1.gz

# (outside the virtual environment)
deactivate

python3 --version
# ubuntu@ip-172-31-2-39:~$ python3 --version
# Python 3.8.10

whereis python3

# python3: /usr/bin/python3 /usr/bin/python3.8 /usr/lib/python3 /usr/lib/python3.8 /usr/lib/python3.9 
# /etc/python3 /etc/python3.8 /usr/local/bin/python3.9 /usr/local/bin/python3.9-config /usr/local/lib/python3.8 
# /usr/local/lib/python3.9 /usr/share/python3 /usr/share/man/man1/python3.1.gz

# notice that the options for the virtual environmnet do not appear in
# whereis python3 
# when outside the virtual environment

# what whereis do?



