# How to install docker in ubuntu?
# https://phoenixnap.com/kb/how-to-install-docker-on-ubuntu-18-04

docker --version

cd docker_study

# how to uninstall docker?
sudo apt remove docker docker-engine docker.io


# https://www.udemy.com/course/docker-mastery/learn/lecture/7742916?start=240#overview

# docker store
# https://hub.docker.com/search?type=plugin

# https://hub.docker.com/editions/community/docker-ce-server-ubuntu

curl -fsSL get.docker.com -o get-docker.sh
sh get-docker.sh

# how to delete a repository ubuntu?
https://askubuntu.com/a/345473

# add an user to the docker account
# we don't need to enter sudo on every command
sudo usermod -aG docker william

sudo docker version
# docker needs root access to the computer for it to be
# able to do things
# 
docker version

# Docker Machine
# install docker machine
# docker machine is deprecated


# https://www.udemy.com/course/docker-mastery/learn/lecture/6489842#questions/14654636

# docker client and docker server
# in Windows we call a background job a "service"
# in Linux and Mac we call it a "Daemon"

sudo docker info
# show information about the docker installation
# it gives information about the host computer
# the number of containers

# https://www.udemy.com/course/docker-mastery/learn/lecture/6489880#questions/14654636

# start a new docker container, it will use some image
# in the case below it will use nginx
sudo docker container run --publish 80:80 nginx 

# we can go to localhost and see the server running

sudo docker container run --publish 8080:80 --detach nginx
# --detach option will make the container run on the background

# after running the command you'll get the docker id for the container
# 8f6ed16e40a16930f5954a7d88e7266cf4c6e554f6cb898b056df115e42b1ea9

# List containers
sudo docker container ls

# CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS              PORTS                                   NAMES
# 8f6ed16e40a1   nginx     "/docker-entrypoint.…"   About a minute ago   Up About a minute   0.0.0.0:8080->80/tcp, :::8080->80/tcp   bold_mcclintock

# let's stop the container that is running
sudo docker container stop 8f6ed16e4

# let's see if the container has stopped
sudo docker container ls


# see all containers 
sudo docker container ls -a

# CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS                      PORTS     NAMES
# 8f6ed16e40a1   nginx     "/docker-entrypoint.…"   3 minutes ago    Exited (0) 48 seconds ago             bold_mcclintock
# 29308cdc1d84   nginx     "/docker-entrypoint.…"   7 minutes ago    Exited (0) 5 minutes ago              ecstatic_lamport
# b353609e4848   nginx     "/docker-entrypoint.…"   14 minutes ago   Exited (0) 7 minutes ago              hardcore_lederberg

# docker container run always creates and starts a new container
# docker container start just starts an existing container
sudo docker container start b353609e4848

sudo docker container ls

sudo docker container stop b353609e4848

sudo docker container start 8f6ed16e40a1







