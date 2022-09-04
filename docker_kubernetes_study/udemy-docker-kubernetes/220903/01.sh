# https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/learn/lecture/11436642#overview

docker run hello-world

# we can include an override command 
docker run busybox echo hi there
# I don't know why it is useful...

docker run busybox ls

docker run hello-world ls
# docker: Error response from daemon: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: exec: "ls": executable file not found in $PATH: unknown.
# ERRO[0004] error waiting for container: context canceled 
# this happens because inside the hello-world image, there is no executable for ls
# so in images where the ls executable exists, this command will not fail

docker run ubuntu ls

# this command will for a longer time
docker run busybox ping google.com
# PING google.com (172.217.28.14): 56 data bytes
# 64 bytes from 172.217.28.14: seq=0 ttl=115 time=30.079 ms
# 64 bytes from 172.217.28.14: seq=1 ttl=115 time=19.507 ms
# 64 bytes from 172.217.28.14: seq=2 ttl=115 time=21.890 ms
# 64 bytes from 172.217.28.14: seq=3 ttl=115 time=44.468 ms
# ^C
# --- google.com ping statistics ---
# 4 packets transmitted, 4 packets received, 0% packet loss
# round-trip min/avg/max = 19.507/28.986/44.468 ms

# two commands
docker create <container name>
docker start <container name>

# docker run will execute both of the commands above
docker run <container name>

# an example with redis
docker run --name my-redis-container redis
docker stop my-redis-container 
docker rm my-redis-container 

docker exec -t my-redis-container redis-cli 

docker exec -t my-redis-container sh
docker exec -t my-redis-container /bin/bash

# https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/learn/lecture/11436686#overview


docker images

mkdir redis-image
cd redis-image

touch Dockerfile

ls

# to give a name to the image?
docker build .

# Sending build context to Docker daemon  2.048kB
# Step 1/3 : FROM alpine
#  ---> e66264b98777
# Step 2/3 : RUN apk add --update redis
#  ---> Using cache
#  ---> c1bc80bbee2e
# Step 3/3 : CMD ["redis-server"]
#  ---> Using cache
#  ---> 404732503209
# Successfully built 404732503209

# this will start a redis server
docker run  404732503209


# use -t (tag) to specify the name of the image
docker build -t william/my-docker-image .

# create a docker container, specify the name
docker run --name my-docker-container my-docker-image 

docker rm my-docker-container


# convention for including a tag in the docker image
<docker_id>/<name of project>:<version>
# and example
williamszk/redis:latest

docker build -t williamszk/redis:latest .
docker run --name my-container williamszk/redis:latest

docker rm my-container















