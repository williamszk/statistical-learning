
# https://hub.docker.com/r/jenkins/jenkins

# this command will just download the jenkins image
# remeber to run it in the host machine not inside the container
docker pull jenkins/jenkins:lts

# william@william-ThinkPad-T450:~$ docker pull jenkins/jenkins:lts
# lts: Pulling from jenkins/jenkins
# dbba69284b27: Pull complete 
# 7a9cfc1d8bc9: Pull complete 
# 714fad1b5f60: Extracting [==================================================>]  45.96kB/45.96kB
# 1c33b24d149a: Download complete 
# ae5685b28918: Download complete 
# 559d6c32b276: Download complete 
# 59d799692e51: Download complete 
# 37c3ff68dde1: Download complete 
# 0b319955f911: Download complete 
# 633e98b0c3ff: Download complete 
# afdef6b9454b: Download complete 
# c9fc43dc7764: Downloading [=============================================>     ]  69.25MB/76.44MB
# 978ba18a6875: Download complete 
# 8a7228030cbd: Download complete 
# 02faeb6b9508: Download complete 
# 4feb05403fe4: Download complete 
# c81d57bc88d8: Download complete 


# to find the docker images that we already have installed
docker images

# william@william-ThinkPad-T450:~$ docker images
# REPOSITORY                    TAG       IMAGE ID       CREATED        SIZE
# jenkins/jenkins               lts       fd576e09d155   4 days ago     464MB
# ubuntu                        latest    d13c942271d6   3 months ago   72.8MB
# gcr.io/k8s-minikube/kicbase   v0.0.29   64d09634c60d   3 months ago   1.14GB
# nginx                         latest    87a94228f133   6 months ago   133MB


# where docker is saving the images?
docker info | grep -i root

# william@william-ThinkPad-T450:~$ docker info | grep -i root
#  Docker Root Dir: /var/lib/docker

# how much space is docker taking?
sudo du -sh /var/lib/docker
# I think -s will take only the directories in the firs level

# william@william-ThinkPad-T450:~$ sudo du -sh /var/lib/docker
# 35G     /var/lib/docker

# 35G 
# this is how much docker is taking of space
# which I think include the space that all repositories are taking









