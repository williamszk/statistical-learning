


# docker
# droplet - digital ocean - centos
ssh -i "C:\Users\william.suzuki\.ssh\id_rsa" root@198.199.122.147


# how to see centos version?
cat /etc/centos-release
# CentOS Linux release 8.5.2111

# install docker in centos
# https://docs.docker.com/engine/install/centos/

# Uninstall old versions
sudo yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine

# It’s OK if yum reports that none of these packages are installed.

# The contents of /var/lib/docker/, including images, containers, volumes, and networks, are preserved. 
# The Docker Engine package is now called docker-ce.

# https://docs.docker.com/engine/install/centos/#install-using-the-repository
# you need to set up the Docker repository
# Afterward, you can install and update Docker from the repository.
# Install the yum-utils package (which provides the yum-config-manager utility) and set up the stable repository.

sudo yum install -y yum-utils

sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

# Install the latest version of Docker Engine and containerd
sudo yum install docker-ce docker-ce-cli containerd.io


# how to see if a program is running with systemctl?
sudo systemctl is-active docker
# inactive

# Start Docker.
sudo systemctl start docker

# Verify that Docker Engine is installed correctly by running the hello-world image.
sudo docker run hello-world

# Run Ubuntu container inside a VM in digital ocean which is a centos...
docker run -it ubuntu bash

# how to list containers?
sudo docker container ps -a
# [root@my-centos-server-droplet ~]# sudo docker container ps -a
# CONTAINER ID   IMAGE         COMMAND    CREATED              STATUS                          PORTS     NAMES
# e03891e54022   ubuntu        "bash"     30 seconds ago       Exited (0) 23 seconds ago                 nostalgic_jang
# 4669705c7d83   hello-world   "/hello"   About a minute ago   Exited (0) About a minute ago             happy_wilbur 

# Course in Docker and Kubernetes
# https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/learn/lecture/11436648?start=0#overview

# How to delete a container?
sudo docker container rm e03891e54022
sudo docker container ps -a
sudo docker container rm 4669705c7d83
sudo docker container ps -a

sudo docker ps
docker ps
docker ps -a

docker run busybox echo hi there!

docker ps -a
docker container rm 700cbb9d4dfa
docker ps -a

docker run busybox ping google.com
docker ps -a

docker ps --all

# https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/learn/lecture/11436650#overview
# Container Lifecycle
# The docker run creates a new container
# docker start and docker stop will act on an existing container
# docker run = docker create + docker start

docker run busybox echo "this is a test with docker run"
docker ps -a
docker start -a 4c6a74821299
docker ps -a

docker create hello-world
docker ps -a
docker start -a c985bc4fe8b6
# we need the -a to make the start command work
# the -a will watch for any output from the contaner
# and print to the terminal
docker ps -a

# https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/learn/lecture/11436652#overview
# Restartig a stopped container
docker run busybox echo "hello there!"
docker ps -a
docker start -a 2e1625a2edcb

# https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/learn/lecture/11436656#overview
# Removing stopped container
ssh -i "C:\Users\william.suzuki\.ssh\id_rsa" root@198.199.122.147

docker ps -a
# we can delete almost everything that we are not using all at once...
docker system prune

# [root@my-centos-server-droplet ~]# docker system prune
# WARNING! This will remove:
#   - all stopped containers
#   - all networks not used by at least one container
#   - all dangling images
#   - all dangling build cache

# Are you sure you want to continue? [y/N] y

docker ps -a
# there are no more containers in the list

# https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/learn/lecture/11436660#overview
# Retrieving Log Outputs
docker create busybox echo "This is just a test..."
docker ps -a

docker start f93b6afdc365
# this will not show output
docker logs f93b6afdc365
# this will show the output of the container
# this will not start or run the container, this will just print the prints
# of the container

# https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/learn/lecture/11436664#overview
# Stopping containers
docker create busybox ping google.com
docker start 681266ca
docker ps -a
# [root@my-centos-server-droplet ~]# docker ps -a
# CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS                     PORTS     NAMES
# 681266ca0ae0   busybox   "ping google.com"        17 seconds ago   Up 3 seconds                         nostalgic_noether
# f93b6afdc365   busybox   "echo 'This is just …"   3 minutes ago    Exited (0) 2 minutes ago             modest_greider

# the container that pings google will continue indefinitely
# we need to stop the container
docker ps -a
docker container stop 681266ca0ae0
# docker stop 681266ca0ae0

docker ps -a
# CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS                        PORTS     NAMES
# 681266ca0ae0   busybox   "ping google.com"        About a minute ago   Exited (137) 14 seconds ago             nostalgic_noether
docker logs 681266ca0ae0
# [root@my-centos-server-droplet ~]# docker logs 681266ca0ae0
# PING google.com (142.250.81.238): 56 data bytes
# 64 bytes from 142.250.81.238: seq=0 ttl=116 time=1.705 ms
# 64 bytes from 142.250.81.238: seq=1 ttl=116 time=1.350 ms
# 64 bytes from 142.250.81.238: seq=2 ttl=116 time=1.329 ms
# 64 bytes from 142.250.81.238: seq=3 ttl=116 time=1.351 ms
# 64 bytes from 142.250.81.238: seq=4 ttl=116 time=1.411 ms
# 64 bytes from 142.250.81.238: seq=5 ttl=116 time=1.375 ms
# 64 bytes from 142.250.81.238: seq=6 ttl=116 time=3.188 ms
# 64 bytes from 142.250.81.238: seq=7 ttl=116 time=1.376 ms


# docker kill 681266ca0ae0
# docker kill is more rough in stoping the container
# and it may not give time for some process to clean up 
# before stopping
# ideally we use docker stop
# if the container is crashed and is not responding we can use docker kill

# if docker stop does not work in 10s, docker will kill the process

docker ps -a
docker start 681266ca0ae0
docker ps
docker stop 681266ca0ae0

docker start 681266ca0ae0
docker ps
docker kill 681266ca0ae0
docker ps -a
docker logs 681266ca0ae0




