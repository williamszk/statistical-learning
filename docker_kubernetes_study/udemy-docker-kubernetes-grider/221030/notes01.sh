docker run hello-world

# https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/learn/lecture/11436646#overview

docker run busybox echo hi there

# https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/learn/lecture/11436678#overview

# https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/learn/lecture/11436686#overview

touch Dockerfile

# -t is tag, it gives a name to the image
docker build -t my-docker-image . 
# build -t my-docker-image .
# Sending build context to Docker daemon  3.072kB
# Step 1/3 : FROM alpine
#  ---> e66264b98777
# Step 2/3 : RUN apk add --update redis
#  ---> Using cache
#  ---> c1bc80bbee2e
# Step 3/3 : CMD ["redis-server"]
#  ---> Using cache
#  ---> 404732503209
# Successfully built 404732503209
# Successfully tagged my-docker-image:latest


docker run my-docker-image
# 1:C 30 Oct 2022 22:33:56.358 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
# 1:C 30 Oct 2022 22:33:56.358 # Redis version=7.0.2, bits=64, commit=2ed046f5, modified=0, pid=1, just started
# 1:C 30 Oct 2022 22:33:56.358 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
# 1:M 30 Oct 2022 22:33:56.359 * monotonic clock: POSIX clock_gettime
# 1:M 30 Oct 2022 22:33:56.365 * Running mode=standalone, port=6379.
# 1:M 30 Oct 2022 22:33:56.365 # Server initialized
# 1:M 30 Oct 2022 22:33:56.365 * Ready to accept connections


mkdir simpleweb
cd simpleweb
npm init -y

npm i express
touch index.js

touch Dockerfile

docker image rm my-docker-image

docker build -t my-docker-image . 
docker run -d --name my-docker-container my-docker-image 
docker exec -it my-docker-container sh
ls
docker stop my-docker-container
docker rm my-docker-container

# before using .dockerignore
# /usr/app # ls
# Dockerfile            a_file_to_ignore.txt  index.js              node_modules          package-lock.json     package.json

# after using .dockerignore
# /usr/app # ls
# Dockerfile         index.js           node_modules       package-lock.json  package.json


# stopped at:
# https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/learn/lecture/11436958#overview

