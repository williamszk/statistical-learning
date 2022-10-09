


docker network ls

docker network create my-mongo-network


# start mongodb contaneir
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

docker ps
# CONTAINER ID   IMAGE           COMMAND                  CREATED          STATUS          PORTS                                           NAMES
# 7e7d950e648e   mongo-express   "tini -- /docker-ent…"   14 seconds ago   Up 9 seconds    0.0.0.0:8081->8081/tcp, :::8081->8081/tcp       my-mongo-express
# 9341786c6ab9   mongo           "docker-entrypoint.s…"   22 seconds ago   Up 17 seconds   0.0.0.0:27017->27017/tcp, :::27017->27017/tcp   my-mongodb

# we can access mongo-express using the browser
localhost:8081

# we can turn on the application
nodemon server.js


docker logs my-mongo-express

# Do all over again
docker stop my-mongodb
docker stop my-mongo-express

docker rm my-mongodb
docker rm my-mongo-express

docker network rm my-mongo-network

# ---------------------------------------------------------------------------- #
# The mongo-express message when it is working

# Mongo Express server listening at http://0.0.0.0:8081
# Server is open to allow connections from anyone (0.0.0.0)
# basicAuth credentials are "admin:pass", it is recommended you change this in your config.js!

# ---------------------------------------------------------------------------- #
# This is what happens if we set the password wrong in mongo-express

# Could not connect to database using connectionString: mongodb://admin:passwords@my-mongodb:27017/"
# (node:8) UnhandledPromiseRejectionWarning: MongoNetworkError: failed to connect to server [my-mongodb:27017] on first connect [Error: connect ECONNREFUSED 172.19.0.2:27017
#     at TCPConnectWrap.afterConnect [as oncomplete] (net.js:1144:16) {
#   name: 'MongoNetworkError'
# }]

# ---------------------------------------------------------------------------- #
# what happens if we use the wrong name for the network?
# the following errors appears:
# bb756db34f915eb9085e1b039901bebdee4a04eeaa777159463e194973faf53a
# docker: Error response from daemon: network my-mongo-network-a not found.
# the container is created but it is not running
# ---------------------------------------------------------------------------- #







