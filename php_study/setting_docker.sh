systemctl status docker

docker ps -a

# how to run a docker container but set the name of the container?
docker run --name php_study -it ubuntu /bin/bash

docker ps -a
# CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS                     PORTS     NAMES
# 1e0366fd6f03   ubuntu    "/bin/bash"   13 seconds ago   Exited (0) 4 seconds ago             php_study
# 2becc6d8ccd6   ubuntu    "/bin/bash"   3 days ago       Exited (0) 3 days ago                interesting_villani

docker start php_study
docker ps
# william@william-ThinkPad-T450:~/Documents/statistical-learning/php_study$ docker ps
# CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS         PORTS     NAMES
# 1e0366fd6f03   ubuntu    "/bin/bash"   46 seconds ago   Up 7 seconds             php_study

docker exec -it php_study /bin/bash

cd ~
ls -la
# root@1e0366fd6f03:~# ls -la
# total 20
# drwx------ 1 root root 4096 Jan 16 17:06 .
# drwxr-xr-x 1 root root 4096 Jan 16 17:06 ..
# -rw------- 1 root root    3 Jan 16 17:06 .bash_history
# -rw-r--r-- 1 root root 3106 Dec  5  2019 .bashrc
# -rw-r--r-- 1 root root  161 Dec  5  2019 .profile







