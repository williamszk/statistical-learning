# Notes about docker compose

docker-compose -f mongo.yaml up

# -d for detached
docker-compose -f mongo.yaml up -d

# Creating network "techworld-js-docker-demo-app_default" with the default driver
# Creating techworld-js-docker-demo-app_my-mongo-express_1 ... done
# Creating techworld-js-docker-demo-app_my-mongodb_1       ... done

# docker compose will create a network if none is specified
# and it will change the name of the containers


docker network ls
# NETWORK ID     NAME                                   DRIVER    SCOPE
# 3e983e3595d0   bridge                                 bridge    local
# 9d7b005025d0   host                                   host      local
# 21b5fac800f4   minikube                               bridge    local
# 46cd60266d08   my-mongo-network                       bridge    local
# ff4c8d7ab631   none                                   null      local
# 2c436e567aaa   techworld-js-docker-demo-app_default   bridge    local

# techworld-js-docker-demo-app_my-mongo-express_1
# techworld-js-docker-demo-app_my-mongodb_1

docker stop techworld-js-docker-demo-app_my-mongo-express_1
docker stop techworld-js-docker-demo-app_my-mongodb_1

docker rm techworld-js-docker-demo-app_my-mongo-express_1
docker rm techworld-js-docker-demo-app_my-mongodb_1

docker network rm techworld-js-docker-demo-app_default

# how to persist data using containers?
# we use container volumes

# we can use the down command to turn off all containers
docker-compose -f mongo.yaml down
# so we don't need to use the usual docker commands by themselves
# we can use docker compose commands


# checkpoint:
# https://youtu.be/3c-iBn73dDE?t=6120 

# Docker Image
# Dockerfile



# call docker compose with all 3 containers now
# docker-compose -f mongo-node.yaml up -d
docker-compose -f mongo-node.yaml up
docker-compose -f mongo-node.yaml down
