

docker build -t my-app:1.0 .
# -t is the name of the image 
# what comes after : is the tag
# we could write 1.0, version-1.0

# the other parameter is the location of the dockerfile
# in this case we execute in the location of the Dockerfile itself

# see that the image that you created is in the list of docker images
# available to create containers
docker images
# REPOSITORY                    TAG         IMAGE ID       CREATED          SIZE
# my-app                        1.0         d6ac7a002c6b   41 seconds ago   130MB
# redis                         latest      2e50d70ba706   7 days ago       117MB
# mongo                         latest      c8b57c4bf7e3   2 weeks ago      701MB


# let's create a container using this image
docker run -d -p 3000:3000 --name my-app-container my-app:1.0

docker logs my-app-container

# remove <none> images
docker rmi $(docker images -f "dangling=true" -q)

docker stop my-app-container
docker rm my-app-container

# maybe we can use 
# docker images prune
# this doesn't work


docker network create my-mongo-network

docker run -d \
    --name my-mongodb \
    -p 27017:27017 \
    --network my-mongo-network \
    -e MONGO_INITDB_ROOT_USERNAME=admin \
    -e MONGO_INITDB_ROOT_PASSWORD=password \
    mongo


docker run -d \
    --name my-mongo-express \
    -p 8081:8081 \
    --network my-mongo-network \
    -e ME_CONFIG_MONGODB_SERVER=my-mongodb \
    -e ME_CONFIG_MONGODB_ADMINUSERNAME=admin \
    -e ME_CONFIG_MONGODB_ADMINPASSWORD=password \
    mongo-express

docker run -d -p 3000:3000 --name my-app-container my-app:1.0

# stop and delete
docker stop my-mongodb
docker stop my-mongo-express

docker rm my-mongodb
docker rm my-mongo-express

docker network rm my-mongo-network


# lets look inside the env variables of the container
# that we created
docker exec -it my-app-container /bin/sh

env
# /home/app # env
# NODE_VERSION=14.19.3
# HOSTNAME=b54163707f03
# YARN_VERSION=1.22.19
# SHLVL=1
# HOME=/root
# MONGO_DB_USERNAME=admin
# TERM=xterm
# PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
# MONGO_DB_PWD=password
# PWD=/home/app



