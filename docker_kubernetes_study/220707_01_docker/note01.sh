
# https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/learn/lecture/11436686#overview


mkdir redis-image

cd redis-image

touch Dockerfile

docker build .
# Sending build context to Docker daemon  2.048kB
# Step 1/3 : FROM alpine
#  ---> e66264b98777
# Step 2/3 : RUN apk add --update redis
#  ---> Running in d787c964db4b
# fetch https://dl-cdn.alpinelinux.org/alpine/v3.16/main/x86_64/APKINDEX.tar.gz
# fetch https://dl-cdn.alpinelinux.org/alpine/v3.16/community/x86_64/APKINDEX.tar.gz
# (1/1) Installing redis (7.0.2-r0)
# Executing redis-7.0.2-r0.pre-install
# Executing redis-7.0.2-r0.post-install
# Executing busybox-1.35.0-r13.trigger
# OK: 9 MiB in 15 packages
# Removing intermediate container d787c964db4b
#  ---> 103c7f59815d
# Step 3/3 : CMD ["redis-server"]
#  ---> Running in 1c6c214f8994
# Removing intermediate container 1c6c214f8994
#  ---> 5a94c82ce78e
# Successfully built 5a94c82ce78e

docker run 5a94c82ce78e
# 1:C 07 Jul 2022 21:59:11.536 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
# 1:C 07 Jul 2022 21:59:11.536 # Redis version=7.0.2, bits=64, commit=2ed046f5, modified=0, pid=1, just started
# 1:C 07 Jul 2022 21:59:11.536 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
# 1:M 07 Jul 2022 21:59:11.538 * monotonic clock: POSIX clock_gettime
# 1:M 07 Jul 2022 21:59:11.539 * Running mode=standalone, port=6379.
# 1:M 07 Jul 2022 21:59:11.539 # Server initialized
# 1:M 07 Jul 2022 21:59:11.540 * Ready to accept connections

# course:
# https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/learn/lecture/11436696#overview 


docker build -t my-image-repository/my-redis-image:1.0 .

# Next:
# https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/learn/lecture/11436722#overview