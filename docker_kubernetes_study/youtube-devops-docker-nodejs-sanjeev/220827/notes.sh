

# https://www.youtube.com/watch?v=jotpVtFwYBk&ab_channel=SanjeevThiyagarajan

cd 220827_01_node_docker
npm init -y
npm i express
touch index.js

nodemon index.js


# build docker container
docker build -t william/my-docker-image .
docker run -d --name my-container -p 3000:3000 william/my-docker-image
docker stop my-container 
docker rm my-container

# using docker-compose
docker-compose up -d --build
docker-compose stop
docker-compose start
docker-compose down





# Stopped at:
# 
# https://youtu.be/jotpVtFwYBk?t=342

