# https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/learn/lecture/11436666?start=15#overview
# Multi command containers


# Redis and Redis-CLI
# 

# we need to use a VM
ssh -i "C:\Users\william.suzuki\.ssh\id_rsa" root@198.199.122.147
# this is the centos in digital ocean
# the credit will expire in Jan 18th... I'll need to use another VM

# docker run redis
# docker: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?.
# See 'docker run --help'.

# Start Docker.
sudo systemctl start docker

docker run redis
# 1:M 07 Jan 2022 02:17:32.413 # Server initialized
# 1:M 07 Jan 2022 02:17:32.413 # WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
# 1:M 07 Jan 2022 02:17:32.414 * Ready to accept connections

tmux
# [root@my-centos-server-droplet ~]# tmux
# -bash: tmux: command not found

sudo yum install tmux

tmux

docker container ps -a
# CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS                          PORTS     NAMES
# af490b4ad243   redis     "docker-entrypoint.s…"   About a minute ago   Exited (0) About a minute ago             flamboyant_einstein
# 681266ca0ae0   busybox   "ping google.com"        3 weeks ago          Exited (137) 3 weeks ago                  nostalgic_noether  
# f93b6afdc365   busybox   "echo 'This is just …"   3 weeks ago          Exited (0) 3 weeks ago                    modest_greider   


docker run redis
# ....
# 1:M 07 Jan 2022 02:19:34.598 # WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
# 1:M 07 Jan 2022 02:19:34.598 * Ready to accept connections

# on another tmux pane, run Redis CLI
# we need to use the redis-cli inside the same container where the redis server is running

# https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/learn/lecture/11436668#overview
# Executing commands in running containers

# to execute a command inside another container
# docker exec
# docker exec -it <container id> <command>

# what is the redis container?
docker container ps -a
# CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS                     PORTS      NAMES
# fd94b5c367be   redis     "docker-entrypoint.s…"   6 minutes ago   Up 6 minutes               6379/tcp   zen_wright
# af490b4ad243   redis     "docker-entrypoint.s…"   8 minutes ago   Exited (0) 7 minutes ago              flamboyant_einstein
# 681266ca0ae0   busybox   "ping google.com"        3 weeks ago     Exited (137) 3 weeks ago              nostalgic_noether  
# f93b6afdc365   busybox   "echo 'This is just …"   3 weeks ago     Exited (0) 3 weeks ago                modest_greider 

# it is the zen_wright, fd94b5c367be

docker exec -it fd94b5c367be redis-cli
# [root@my-centos-server-droplet ~]# docker exec -it fd94b5c367be redis-cli
# 127.0.0.1:6379> 

# now we can use redis-cli which is running inside the container

set myvalue 5

get myvalue

# 127.0.0.1:6379> set myvalue 5
# OK
# 127.0.0.1:6379> get myvalue
# "5"
# 127.0.0.1:6379>

# what -it means?

# https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/learn/lecture/11436670#overview
# The Purpose of the IT flag

# -i = attach my terminal to the container
# -t = show text in pretty manner


# https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/learn/lecture/11436674#overview
# Get a command prompt in a container

docker exec -it fd94b5c367be sh
# the "sh" command is very important

# now we are inside the container
ls -a
# .  ..

cd /
ls -a
# cd /
# ls -a
# .  ..  .dockerenv  bin  boot  data  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var

echo hi there
# echo hi there
# hi there 

pwd
# pwd
# /   

cd ~
pwd
# pwd 
# /root

export b=5
echo $b
# export b=5
# echo $b     
# 5

redis-cli
# 127.0.0.1:6379> 

# use ctrl-d to exist the container

# sh is just a shell program, we could use bash, zsh or powershell

docker exec -it fd94b5c367be bash
# root@fd94b5c367be:/data#

# the terminal is a litte prettier
# and we can use the tipical commands of a unix terminal
docker exec -it fd94b5c367be zsh
# [root@my-centos-server-droplet ~]# docker exec -it fd94b5c367be zsh
# OCI runtime exec failed: exec failed: container_linux.go:380: starting container process caused: exec: "zsh": executable file not found in $PATH: unknown

# https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/learn/lecture/11436676#overview
# Starting with a Shell

docker run -it busybox sh
# this command will create and start a new container of image busybox, then we will enter into it, and use sh

# / # ls
# bin   dev   etc   home  proc  root  sys   tmp   usr   var

ping google.com
# / # ping google.com
# PING google.com (142.250.64.78): 56 data bytes
# 64 bytes from 142.250.64.78: seq=0 ttl=116 time=1.437 ms
# 64 bytes from 142.250.64.78: seq=1 ttl=116 time=0.960 ms
# 64 bytes from 142.250.64.78: seq=2 ttl=116 time=1.056 ms
# 64 bytes from 142.250.64.78: seq=3 ttl=116 time=0.934 ms

# https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/learn/lecture/11436678#overview
# Container Isolation

# In this video we make an experiment where we create two containers and we change the 
# disk of one container and see if this affects the other container, it does not
# just an exercise

docker run -it busybox sh

ls
# / # ls
# bin   dev   etc   home  proc  root  sys   tmp   usr   var


# in another terminal pane
docker run -it busybox sh

ls
# / # ls
# bin   dev   etc   home  proc  root  sys   tmp   usr   var

# In another pane 
docker ps -a
# CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS                      PORTS      NAMES
# 6007409643b5   busybox   "sh"                     35 seconds ago       Up 35 seconds                          unruffled_brahmagupta
# c2c35190407a   busybox   "sh"                     About a minute ago   Up About a minute                      upbeat_beaver        

# on the first pane
touch hithere.py
ls
# / # ls
# bin         dev         etc         hithere.py  home        proc        root        sys         tmp         usr         var

# on the second pane
ls
# / # ls
# bin   dev   etc   home  proc  root  sys   tmp   usr   var

# the two containers have seperate file systems and there is complete isolation between the two

# next class is Creating Docker Images
# https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/learn/lecture/11436686#overview

















