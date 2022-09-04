# we need to turn on the vm that we use
# now I'm using a centos vm on digital ocean
# but we can use any vm in any cloud provider

# ssh into the vm
ssh -i "C:\Users\william.suzuki\.ssh\id_rsa" root@198.199.122.147

# check the status of the docker daemon
sudo systemctl status docker
# [root@my-centos-server-droplet ~]# sudo systemctl status docker
# ● docker.service - Docker Application Container Engine
#    Loaded: loaded (/usr/lib/systemd/system/docker.service; disabled; vendor preset: disabled)
#    Active: inactive (dead)
#      Docs: https://docs.docker.com

# the docker daemon is off

# turn on the dockear daemon
sudo systemctl start docker

sudo systemctl status docker
# ● docker.service - Docker Application Container Engine
#    Loaded: loaded (/usr/lib/systemd/system/docker.service; disabled; vendor preset: disabled)
#    Active: active (running) since Fri 2022-01-07 14:01:16 UTC; 7s ago
#      Docs: https://docs.docker.com
#  Main PID: 1412 (dockerd)
#     Tasks: 8
#    Memory: 132.9M
#    CGroup: /system.slice/docker.service
#            └─1412 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock  


# https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/learn/lecture/11436692#overview
# Building a Dockerfile

# here we build from scratch a docker image that is like the redis image
#
ls

# [root@my-centos-server-droplet ~]# ls
# dnsrecon  go  original-ks.cfg  wordlists

# I've been studying catch the flag in this VM too

mkdir redis-image
cd redis-image
touch Dockerfile

# we need to edit the docker file now
# I use vim

sudo yum install vim

vim Dockerfile

# I write the Dockerfile content here
# then I copy into vim

# begin Dockerfile -------------------------------------------

# Use an existing docker image as a base
FROM alpine

# Download and install a dependency
RUN apk add --update redis

# Tell the image what to do when it starts as a container
CMD ["redis-server"]

# end Dockerfile -------------------------------------------

# paste into the Dockerfile
# 
# then, type the command:
docker build .
# [root@my-centos-server-droplet redis-image]# docker build .
# Sending build context to Docker daemon  2.048kB
# Step 1/3 : FROM alpine
# latest: Pulling from library/alpine
# 59bf1c3509f3: Pull complete
# Digest: sha256:21a3deaa0d32a8057914f36584b5288d2e5ecc984380bc0118285c70fa8c9300
# Status: Downloaded newer image for alpine:latest
#  ---> c059bfaa849c
# Step 2/3 : RUN apk add --update redis
#  ---> Running in 85e0a2e1fd64
# fetch https://dl-cdn.alpinelinux.org/alpine/v3.15/main/x86_64/APKINDEX.tar.gz
# fetch https://dl-cdn.alpinelinux.org/alpine/v3.15/community/x86_64/APKINDEX.tar.gz
# (1/1) Installing redis (6.2.6-r0)
# Executing redis-6.2.6-r0.pre-install
# Executing redis-6.2.6-r0.post-install
# Executing busybox-1.34.1-r3.trigger
# OK: 8 MiB in 15 packages
# Removing intermediate container 85e0a2e1fd64
#  ---> 6b75a9f27dc8
# Step 3/3 : CMD ["redis-server"]
#  ---> Running in 381fcef0143f
# Removing intermediate container 381fcef0143f
#  ---> a708deae5d92
# Successfully built a708deae5d92


# a708deae5d92 this is the id of our docker image

docker run a708deae5d92

# [root@my-centos-server-droplet redis-image]# docker run a708deae5d92
# 1:C 07 Jan 2022 14:16:44.882 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
# 1:C 07 Jan 2022 14:16:44.882 # Redis version=6.2.6, bits=64, commit=b39e1241, modified=0, pid=1, just started
# 1:C 07 Jan 2022 14:16:44.882 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
# 1:M 07 Jan 2022 14:16:44.884 * monotonic clock: POSIX clock_gettime
# 1:M 07 Jan 2022 14:16:44.884 * Running mode=standalone, port=6379.
# 1:M 07 Jan 2022 14:16:44.885 # WARNING: The TCP backlog setting of 511 cannot be enforced because /proc/sys/net/core/somaxconn is set to the lower value of 128.
# 1:M 07 Jan 2022 14:16:44.885 # Server initialized
# 1:M 07 Jan 2022 14:16:44.885 # WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
# 1:M 07 Jan 2022 14:16:44.885 * Ready to accept connections


# stopped at:
# https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/learn/lecture/11436702#overview
# What's a Base Image?

# it seems that busybox is a embeded operating system and alpine is a light weight linux operating system
# does busysbox comes with bash? or sh?

# does alpine come with bash? or sh?

# delete all contaiers...




# how to list the docker images that we have?





