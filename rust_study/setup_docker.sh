# create a docker container for rust development

systemctl status docker

docker ps -a

docker run --name rust_study -it ubuntu /bin/bash

# now we are inside the docker rust_study

# the next step is to use vscode inside the docker container

# docker ps -a

# docker exec -it rust_study /bin/bash

apt update
apt install git -y
apt install curl -y
apt install build-essential -y # this is needed so that we have gcc needed for rustc

cd ~

git clone https://github.com/williamszk/statistical-learning.git


# I had a problem with vscode not connecting with the container
# I just destroyed and created it again


# how to install rust in linux?

# https://www.rust-lang.org/tools/install

cd

curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

cd /root/statistical-learning/rust_study

rustc --version
# rustc 1.58.1 (db9d1b20b 2022-01-20)










