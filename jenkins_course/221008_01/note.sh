
# https://www.udemy.com/course/jenkins-from-zero-to-hero/learn/lecture/12847804#overview
mkdir jenkins-data

mkdir jenkins_home

# user 1000

# run the command below to see users
id
# uid=1000(william) gid=1000(william) groups=1000(william),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),121(lpadmin),132(lxd),133(sambashare),134(docker)

# spin up the container(s)
docker-compose up -d

# william@william-ThinkPad-T450:~/Documents/statistical-learning/jenkins_course/221008_01$ docker ps
# CONTAINER ID   IMAGE             COMMAND                  CREATED          STATUS         PORTS                                                  NAMES
# f5874b5d0d57   jenkins/jenkins   "/usr/bin/tini -- /u…"   15 seconds ago   Up 6 seconds   0.0.0.0:8080->8080/tcp, :::8080->8080/tcp, 50000/tcp   jenkins

# read the logs from the container
docker logs -f jenkins

# Jenkins initial setup is required. An admin user has been created and a password generated.
# Please use the following password to proceed to installation:

# 830e310b9c014a5bb395b8699d877399

# This may also be found at: /var/jenkins_home/secrets/initialAdminPassword

# We need to use this information
# In the browser we go to: localhost:8080
# there we need to use the token to confirm that we are the owners of the 
# jenkins server 

# ----------------------------------------------------
# Create first admin user
# william
# 830e310b9c014a5bb39

# another tutorial
# https://youtu.be/nCKxl7Q_20I?t=417


# -------------------
# stopped at:
# https://youtu.be/nCKxl7Q_20I?t=1927
