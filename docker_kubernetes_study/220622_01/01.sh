# Docker repository
# Docker Hub is a public repository
# in a private repository we would have to use authentication
# to get acces to the Docker Images

docker run postgres:9.6
docker run postgre:10.10
# we can run many version of postgres in my machine 
# at the same time

docker ps -a

# there is a difference between a Docker Image and a Docker Container
# it is like a Class and an Instance
# the image is artifact that we can move around

# docker pull
# docker run
# docker start
# docker stop
# docker ps

# inside the docker container we can have defined:
# a file system
# environment configuration
# application image 
# we can bind a port to the container

# this will download the docker image for redis
# from docker hub
docker pull redis

# check which images we already have downloaded
docker images
# REPOSITORY                    TAG       IMAGE ID       CREATED        SIZE
# jenkins/jenkins               lts       fd576e09d155   2 months ago   464MB
# ubuntu                        latest    d13c942271d6   5 months ago   72.8MB
# gcr.io/k8s-minikube/kicbase   v0.0.29   64d09634c60d   6 months ago   1.14GB
# nginx                         latest    87a94228f133   8 months ago   133MB

# this will start the container in attached mode
docker run redis
# so the terminal will be blocked for use

# we can start the container in detached mode
docker run -d redis

# can we use -d when starting a container?
docker start -d jovial_carver
# unknown shorthand flag: 'd' in -d
# See 'docker start --help'.
# docker rm jovial_carver
# we can't start a container using the detached mode
# we need to create a new container

# we can run two docker containers with different versions
# of redis
docker run -d redis:5.0.6
docker run -d redis:4.0
# CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS          PORTS      NAMES
# 3aaf1b52ddff   redis:4.0     "docker-entrypoint.s…"   7 minutes ago    Up 7 minutes    6379/tcp   elated_keldysh
# 46f3e1d7d924   redis:5.0.6   "docker-entrypoint.s…"   11 minutes ago   Up 11 minutes   6379/tcp   adoring_mendel

# note that we are running two versions of redis in different containers

# about ports
# note that both containers are running on the same port
# there is a difference between:
# the container ports
# the host ports

# binding between host port and container port
# how to bind a host port to a container port?

docker stop 3aaf1b52ddff
docker stop 46f3e1d7d924

docker rm 3aaf1b52ddff
docker rm 46f3e1d7d924

# when we create the docker container we need to specify its port binding
docker run -p6000:6379 -d redis:5.0.6
docker run -p6001:6379 -d redis:4.0
# the first port is the host port and the second is the container port


# CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS         PORTS                                       NAMES
# 00f2233a429d   redis:4.0     "docker-entrypoint.s…"   6 seconds ago    Up 2 seconds   0.0.0.0:6001->6379/tcp, :::6001->6379/tcp   dreamy_galois
# ca7907d5cdab   redis:5.0.6   "docker-entrypoint.s…"   11 seconds ago   Up 7 seconds   0.0.0.0:6000->6379/tcp, :::6000->6379/tcp   suspicious_bose

# note in the ports column where we specify the host port and the container port
# 0.0.0.0:6001->6379/tcp
# my host machine port 6001 is bound to the port 6379 of the container

# I don't think that we can start the container with the port bindings

# how can we make two docker containers communicate with each other?

# https://youtu.be/3c-iBn73dDE?t=3440

docker stop dreamy_galois
docker stop suspicious_bose

docker rm dreamy_galois
docker rm suspicious_bose












