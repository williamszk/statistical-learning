

# https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/learn/lecture/11436944#overview

# create a nodejs application 
# and include it inside a container

mkdir simpleweb
cd simpleweb

npm init -y

npm i

touch index.js

touch Dockerfile

docker build -t my-docker-image .


