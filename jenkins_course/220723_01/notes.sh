
# https://www.udemy.com/course/jenkins-from-zero-to-hero/learn/lecture/12847560#overview

docker pull jenkins
docker pull jenkins/jenkins:lts

docker images
# REPOSITORY                           TAG       IMAGE ID       CREATED        SIZE
# jenkins/jenkins                      lts       89b279054578   10 days ago    461MB

# to know where docker is saving the images
docker info | grep -i "root"
# Docker Root Dir: /var/lib/docker
docker info

# how much space docker is using?
sudo su -
sudo du -sh /var/lib/docker

# https://www.udemy.com/course/jenkins-from-zero-to-hero/learn/lecture/12847804#overview

mkdir jenkins
cd jenkins

mkdir jenkins-data
cd jenkins-data

touch docker-compose.yaml
mkdir jenkins_home
echo $PWD

# 1000 is the user id
# $ id
# uid=1000(william) gid=1000(william) groups=1000(william),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),120(lpadmin),132(lxd),133(sambashare),998(docker)
# -R is for recursive
sudo chown 1000:1000 jenkins_home -R
# without this maybe we can not write into the jenkins_home

# start jenkis container
docker-compose up -d
# -d is for detach mode

docker ps
# CONTAINER ID   IMAGE                 COMMAND                  CREATED          STATUS          PORTS                                                  NAMES
# a385505755fc   jenkins/jenkins:lts   "/usr/bin/tini -- /u…"   22 seconds ago   Up 16 seconds   0.0.0.0:8080->8080/tcp, :::8080->8080/tcp, 50000/tcp   jenkins

docker network ls 
# william@william-300E5M-300E5L:~/Documents/statistical-learning/jenkins_course/220723_01/jenkins/jenkins-data$ docker network ls
# NETWORK ID     NAME               DRIVER    SCOPE
# 276e2cb5965b   bridge             bridge    local
# a4c22dea1d06   host               host      local
# 251cef2a77dc   jenkins-data_net   bridge    local
# d54e45b6806e   none               null      local


# I think that -f is for keep trackng of the logs of a container
docker logs -f jenkins
# ******************************************

# Jenkins initial setup is required. An admin user has been created and a password generated.
# Please use the following password to proceed to installation:

# 2da7755dbedb40f28e6fd0dc8ef19da3
# 2da7755dbedb40f28e6fd0dc8ef19da3


# This may also be found at: /var/jenkins_home/secrets/initialAdminPassword

# *************************************************************
# *************************************************************
# *************************************************************

# 2022-07-23 20:51:57.723+0000 [id=49]    INFO    h.m.DownloadService$Downloadable#load: Obtained the updated data file for hudson.tasks.Maven.MavenInstaller
# 2022-07-23 20:51:57.724+0000 [id=49]    INFO    hudson.util.Retrier#start: Performed the action check updates server successfully at the attempt #1
# 2022-07-23 20:51:57.739+0000 [id=49]    INFO    hudson.model.AsyncPeriodicWork#lambda$doRun$1: Finished Download metadata. 47,401 ms
# 2022-07-23 20:51:58.075+0000 [id=30]    INFO    jenkins.InitReactorRunner$1#onAttained: Completed initialization
# 2022-07-23 20:51:58.141+0000 [id=23]    INFO    hudson.lifecycle.Lifecycle#onReady: Jenkins is fully up and running

# we need to go to the localhost:8080 in the browser


# Create First Admin User
# Username: admin
# Password: 2da7755dbedb40f28e6fd0dc8ef19da3
# Full name: Jenkins Admin 
# E-mail address: jenkins@email.com

# https://www.udemy.com/course/jenkins-from-zero-to-hero/learn/lecture/12910700#overview

# DNS

# to stop the jenkins docker-compose
docker-compose stop 

# start the jenkins service using docker-compose
docker-compose start

# to stop and start again a container/service in the docker-compose file
docker-compose restart jenkins

# to delete the containers
docker-compose down
# but this will not delete from the volumes
# so the files will be kept intact
# and we can create the containers again 
# and continue from where left off
docker-compose up -d
# CONTAINER ID   IMAGE                 COMMAND                  CREATED         STATUS         PORTS                                                  NAMES
# a1b4bb8d0f71   jenkins/jenkins:lts   "/usr/bin/tini -- /u…"   6 seconds ago   Up 3 seconds   0.0.0.0:8080->8080/tcp, :::8080->8080/tcp, 50000/tcp   jenkins

# in the browser we can use jenkins in the same way that we had before
# so volumes are very important to not loose all the work



















