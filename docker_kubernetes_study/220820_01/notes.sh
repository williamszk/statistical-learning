

# https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/learn/lecture/11436978?start=15#overview

mkdir visits
cd visits
npm init

touch index.js

npm i express redis@2.8.0
 
touch Dockerfile

docker build .
docker build -t william/my-visits:latest .
# -t is the tag

docker run william/my-visits

docker run redis


# Everything that can be done using docker-compose can be done 
# using the Docker CLI commands
# Let's try to implement the commands in Docker CLI to spin up
# the application with the redis server

docker network create my-visits-network

docker run -d \
    --network my-visits-network \
    --name redis-server \
    redis  

docker run -d \
    --network my-visits-network \
    -p 4001:8081 \
    --name my-nodejs-app \
    william/my-visits 

docker logs my-nodejs-app


docker stop redis-server
docker stop my-nodejs-app

docker rm redis-server
docker rm my-nodejs-app
docker network rm my-visits-network 

# this didn't work...

# =================================================== 

touch docker-compose.yaml

docker-compose up
docker-compose up --build
docker-compose up --build -d


docker-compose start
docker-compose stop

docker-compose down

docker logs visits_node-app_1
# =================================================== 

docker-compose ps
#         Name                       Command               State                    Ports                  
# ---------------------------------------------------------------------------------------------------------
# visits_node-app_1       docker-entrypoint.sh npm start   Up      0.0.0.0:4001->8081/tcp,:::4001->8081/tcp
# # visits_redis-server_1   docker-entrypoint.sh redis ...   Up      6379/tcp  

# https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/learn/lecture/11437010#overview

# =================================================== 





