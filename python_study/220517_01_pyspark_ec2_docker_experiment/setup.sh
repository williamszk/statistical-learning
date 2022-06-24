#
# This code is used to setup the repo that we need to pass and 
# 

sudo yum update
# is yum from fedora/red hat family? yes
# 

# check if git is installed
git --version

# install git
sudo yum install git -y

# clone code directory
git clone https://github.com/williamszk/statistical-learning.git

ls

cd statistical-learning
ls
cd python_study

ls
mkdir 220517_01_pyspark_ec2_docker_experiment
cd 220517_01_pyspark_ec2_docker_experiment
ls
touch 01.ipynb
ls

cd
rm -rf statistical-learning

# made a mistake, the repo should be inside a docker container

# we need to install docker
# https://www.cyberciti.biz/faq/how-to-install-docker-on-amazon-linux-2/

sudo yum search docker
sudo yum info docker

sudo yum install docker

# Add group membership for the default ec2-user so you can run all docker commands without using the sudo command:
sudo usermod -a -G docker ec2-user
id ec2-user
# uid=1000(ec2-user) gid=1000(ec2-user) groups=1000(ec2-user),4(adm),10(wheel),190(systemd-journal),992(docker)
# the ec2-user is included in the docker group


# check if docker is running
sudo systemctl status docker.service
# it is inactive
sudo systemctl start docker.service

# check again
sudo systemctl status docker.service
# it is running


docker ps
# got permission denied
# I'll logout and login again

exit

ssh -i "C:\Users\william.suzuki\Documents\study\aws_study\aws_personal_ubuntu_server_key.pem" ec2-user@ec2-15-228-185-7.sa-east-1.compute.amazonaws.com

docker ps
# now it worked

docker ps -a

# create a docker container
# use a ubuntu image

# https://docs.docker.com/engine/reference/commandline/create/
docker create ubuntu
# this will create but no start the container
# this will download the image latest ubuntu
docker ps -a

# forgot to set the name of the container
docker rm dreamy_dubinsky

# docker create ubuntu --name pyspark

docker ps -a

# the command is wrong
docker rm sharp_mestorf

# this is the correct order
docker create --name pyspark ubuntu
docker ps -a

docker start pyspark

docker ps
# it did not work, the container died right after

docker rm pyspark

# let me test this
docker run -it --name pyspark_study  ubuntu /bin/bash 
# this worked we are inside the container now

# exit the container
exit
docker ps -a
# the status show "exited"

# let's try to start it again
docker start pyspark_study

docker ps -a
# 

# log into the ec2 instance
ssh -i "C:\Users\william.suzuki\Documents\study\aws_study\aws_personal_ubuntu_server_key.pem" ec2-user@ec2-18-231-198-69.sa-east-1.compute.amazonaws.com

docker ps

# docker is turned off
sudo systemctl start docker.service

docker ps -a

docker start pyspark_study

docker ps

# log into the terminal of the container
docker exec -it pyspark_study /bin/bash

# [inside the container]
cd
ls

git --version

apt update
apt install git -y

git clone https://github.com/williamszk/statistical-learning.git

cd statistical-learning

git pull origin master

# test using vscode remote connect to check if we can 
# connect to a container inside a ec2 instance.
# it is possible, I need to first connect with 
# the ec2 instance, and then using the container tab
# of the remote connect, I can choose to connect with the
# container

# we need to install pyspark

ssh -i "C:\Users\william.suzuki\Documents\study\aws_study\aws_personal_ubuntu_server_key.pem" ec2-user@ec2-18-231-198-69.sa-east-1.compute.amazonaws.com
docker exec -it pyspark_study /bin/bash

python3 --version

# 
apt update
apt install python3 -y

cd ~/statistical-learning/python_study
ls

python3 --version

apt install python3.10-venv -y

python3 -m venv .venv


# I find that connecting to a container inside a ec2 instance is not stable
# It would be simpler to simply spin up a vm and then use it as a development environment

