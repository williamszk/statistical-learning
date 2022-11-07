# https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/learn/lecture/11436982#overview

mkdir visits

npm init -y
npm i express 
npm i redis@2.8.0

touch index.js

touch Dockerfile

docker build -t williamszk/visits:latest . 

docker run \
    -d -p 8081:8081 \
    --name my-container-visits \
    williamszk/visits:latest

docker stop my-container-visits
docker rm my-container-visits

docker logs my-container-visits

touch docker-compose.yml

docker-compose up --build
docker-compose up --build -d
docker-compose down
docker-compose start
docker-compose stop

docker-compose ps



