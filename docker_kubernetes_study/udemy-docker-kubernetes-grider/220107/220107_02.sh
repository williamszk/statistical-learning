# https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/learn/lecture/11436702#overview
# What's a Base Image?

# it seems that busybox is a embeded operating system and alpine is a light weight linux operating system
# does busysbox comes with bash? or sh?

# does alpine come with bash? or sh?

# delete all contaiers...


# ssh into the vm
ssh -i "C:\Users\william.suzuki\.ssh\id_rsa" root@198.199.122.147

sudo systemctl status docker
sudo systemctl start docker

docker ps -a

docker start 6007409643b5 # this is a busybox container
docker ps

docker exec -it 6007409643b5 bash
# [root@my-centos-server-droplet ~]# docker exec -it 6007409643b5 bash
# OCI runtime exec failed: exec failed: container_linux.go:380: starting container process caused: exec: "bash": executable file not found in $PATH: unknown

docker exec -it 6007409643b5 sh
# this works in busybox

docker ps -a

docker run -it alpine bash
# [root@my-centos-server-droplet ~]# docker run -it alpine bash
# docker: Error response from daemon: OCI runtime create failed: container_linux.go:380: starting container process caused: exec: "bash": executable file not found in $PATH: unknown.
# ERRO[0000] error waiting for container: context canceled

# bash does exist in alpine

docker ps -a

docker run alpine
docker ps -a

docker start -i 3779e42b3d8a
docker ps -a
# this doesn't work, I need to enter the container

docker exec -it gracious_northcutt sh


docker run -d alpine
docker ps -a
docker run -it alpine /bin/sh
docker ps


# delete all containers
sudo docker container rm 8f6ed16e40a1

docker ps -a
docker stop 6007409643b5

# how to use awk? in the docker ps -a
# I want to delete all turned off containers
docker ps -a

# https://www.grymoire.com/Unix/Awk.html#uh-1

docker ps -a
docker ps -a | awk '{print $1}'
# 02395a20cd9c
# 156a8563963e
# 3779e42b3d8a
# 5a92dad3db24
# cfac48e9ef5c
# 6007409643b5
# c2c35190407a
# 9e94289e1717
# 3dbf7c5d7b1b
# fd94b5c367be
# af490b4ad243
# 681266ca0ae0
# f93b6afdc365

# this will delete all containers
docker container rm $(docker ps -a | awk '{print $1}')
docker ps -a

# https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/learn/lecture/11436706#overview




