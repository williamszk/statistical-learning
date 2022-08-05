
docker pull mongo
docker pull mongo-express

docker network ls
# NETWORK ID     NAME       DRIVER    SCOPE
# 3e983e3595d0   bridge     bridge    local
# 9d7b005025d0   host       host      local
# 21b5fac800f4   minikube   bridge    local
# ff4c8d7ab631   none       null      local

docker network create my-mongo-network
# 51d54b93ac09b5809cfa7f242264844df08cba2e6da01f9c535c8b06ce0f9307

docker network ls
# NETWORK ID     NAME               DRIVER    SCOPE
# 3e983e3595d0   bridge             bridge    local
# 9d7b005025d0   host               host      local
# 21b5fac800f4   minikube           bridge    local
# 51d54b93ac09   my-mongo-network   bridge    local
# ff4c8d7ab631   none               null      local

# start mongodb contaneir
docker run -d \
    -p 27017:27017 \
    --name my-mongodb \
    --network my-mongo-network \
    -e MONGO_INITDB_ROOT_USERNAME=admin \
    -e MONGO_INITDB_ROOT_PASSWORD=password \
    mongo

docker logs my-mongodb

# start mongo-express contaneir
docker run -d \
    -p 8081:8081 \
    --name my-mongo-express \
    --network my-mongo-network \
    -e ME_CONFIG_MONGODB_SERVER=my-mongodb \
    -e ME_CONFIG_MONGODB_ADMINUSERNAME=admin \
    -e ME_CONFIG_MONGODB_ADMINPASSWORD=password \
    mongo-express

# We can set the docker network so that two containers can communicate with each other without the 
# need to use the external ports of the host machine
# We can just specify the network name when creating the container using the --network argument 

# CONTAINER ID   IMAGE           COMMAND                  CREATED          STATUS          PORTS                                           NAMES
# 5243f00986ff   mongo-express   "tini -- /docker-ent…"   53 seconds ago   Up 50 seconds   0.0.0.0:8081->8081/tcp, :::8081->8081/tcp       my-mongo-express
# b9ca67c0e6e7   mongo           "docker-entrypoint.s…"   20 minutes ago   Up 20 minutes   0.0.0.0:27017->27017/tcp, :::27017->27017/tcp   my-mongodb

docker logs my-mongo-express
# Welcome to mongo-express
# ------------------------
# Mongo Express server listening at http://0.0.0.0:8081
# Server is open to allow connections from anyone (0.0.0.0)
# basicAuth credentials are "admin:pass", it is recommended you change this in your config.js!

# we can open now mongo express in the browser in port 8081

localhost:27017

docker logs my-mongodb
docker logs my-mongodb | tail
# this will stream the logs
docker logs my-mongodb -f 

# https://youtu.be/3c-iBn73dDE?t=5377

# Docker Compose
# https://youtu.be/3c-iBn73dDE?t=5390


# 5243f00986ff   mongo-express                         "tini -- /docker-ent…"   3 hours ago    Exited (143) About an hour ago             my-mongo-express
# b9ca67c0e6e7   mongo                                 "docker-entrypoint.s…"   4 hours ago    Exited (0) 8 seconds ago                   my-mongodb

docker start my-mongo-express
docker start my-mongodb

docker rm my-mongo-express
docker rm my-mongodb

docker network rm my-mongo-network