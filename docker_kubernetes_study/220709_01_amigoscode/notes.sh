
docker pull nginx

docker run --name my-nginx-container nginx:latest
docker run --name my-nginx-container -d nginx:latest

docker stop my-nginx-container
docker rm my-nginx-container

# expose ports
docker run --name my-nginx-container -p 8080:80 -d nginx:latest

# we can map two host ports to the container port
docker run --name my-nginx-container -p 3000:80 -p 8080:80 -d nginx:latest

