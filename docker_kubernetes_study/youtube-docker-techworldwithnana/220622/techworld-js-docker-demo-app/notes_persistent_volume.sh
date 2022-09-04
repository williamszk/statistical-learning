# Plug the host's file system to the container's file system
# 

# 3 types of docker volumes

# ============================= #
# Type 1 - Host Volumes
# ============================= #
# docker run
# -v /home/mount/data:/var/lib/mysqldata
# We can choose where in the host file system we set the 

# ============================= #
# Type 2 - Anonymous Volumes
# ============================= #
# Specify only the container's volume:
# docker run
# -v /var/lib/mysql/data
# We don't have control of where exactly in our host machine
# we'll save the persistent data

# ============================= #
# Type 3 - Named Volumes
# ============================= #
# docker run
# -v name:/var/lib/mysql/data
# we can use any name

# Named volumes are the best

docker-compose -f mongo-node-volume.yaml up 
docker-compose -f mongo-node-volume.yaml down

# where are the docker volumes inside the host machine?
/var/lib/docker/volumes
# to enter inside we need to be switch users to root
# sudo su -
# then inside there we can find all volumes, persistent or not

# root@william-ThinkPad-T450:~# cd /var/lib/docker
# root@william-ThinkPad-T450:/var/lib/docker# cd volumes/
# root@william-ThinkPad-T450:/var/lib/docker/volumes# ls
# techworld-js-docker-demo-app_mongo-data


# When we run docker compose
# Creating network "techworld-js-docker-demo-app_default" with the default driver
# Creating techworld-js-docker-demo-app_my-mongo-express_1 ... done
# Creating techworld-js-docker-demo-app_my-mongodb_1       ... done
# Attaching to techworld-js-docker-demo-app_my-mongo-express_1, techworld-js-docker-demo-app_my-mongodb_1




