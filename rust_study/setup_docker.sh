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

cd ~

git clone https://github.com/williamszk/statistical-learning.git


# I had a problem with vscode not connecting with the container
# I just destroyed and created it again















