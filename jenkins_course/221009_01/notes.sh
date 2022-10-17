
mkdir jenkins_home

touch docker-compose.yaml

docker-compose up -d

ca325456451c405aaff0104a5f6f08c2

william
1234
William Suzuki

# create a script outside the container
# then we copy it inside of the container

chmod +x script.sh

./script.sh William Suzuki 

# we could use volumes to share files between the host and the container

docker cp ./script.sh jenkins:/tmp/script.sh

docker exec -it jenkins /bin/bash

# video watching
# https://www.udemy.com/course/jenkins-from-zero-to-hero/learn/lecture/12925870#overview

# 2022-10-11 next video:
# https://www.udemy.com/course/jenkins-from-zero-to-hero/learn/lecture/12925952#overview


# https://www.udemy.com/course/jenkins-from-zero-to-hero/learn/lecture/12925952?start=15#overview

# this directory is a volume for the other container that we'll create
mkdir centos7
touch centos7/Dockerfile

docker pull centos

# create ssh keys
ssh-keygen -f my-remote-key

# we've updated the docker-compose file
# with this command we are going to just build the images
# declared inside this docker-compose file
docker-compose build

# this will read the docker-compose.yaml file and create what is left
docker-compose up -d

docker-compose ps

# enter into the jenkins container
docker exec -it jenkins bash

# [inside jenkins container]
# ssh into the remote-host container
ssh remote_user@remote_host
# we can use the name of the service defined in the docker-compose file
# because docker creates an internal DNS

# now we are inside the remote_host container

# go back to the host machine
# copy the private key of remote_host container into the jenkins container
docker cp ./centos7/my-remote-key jenkins:/tmp/my-remote-key

# we can enter into the jenkins container again
docker exec -it jenkins bash

# then we can ssh into the remote_host container
ssh -i /tmp/my-remote-key remote_user@remote_host
# in this way ssh will not ask for a password

# next video:
# https://www.udemy.com/course/jenkins-from-zero-to-hero/learn/lecture/12925972#overview

docker-compose start


