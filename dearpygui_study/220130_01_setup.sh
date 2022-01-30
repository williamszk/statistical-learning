# first we'll delete the old container
docker ps -a
# (venv) william@william-300E5M-300E5L:~/Documents/statistical-learning$ docker ps -a
# CONTAINER ID   IMAGE     COMMAND       CREATED        STATUS                    PORTS     NAMES
# ba7f51df734d   ubuntu    "/bin/bash"   4 hours ago    Up 32 minutes                       mysql_study_dear
# 0267890844bb   ubuntu    "/bin/bash"   27 hours ago   Exited (0) 14 hours ago             webdev_study
# 0a792f11a2a8   ubuntu    "/bin/bash"   6 days ago     Exited (130) 6 days ago             go_study

docker stop mysql_study_dear
docker rm mysql_study_dear

docker ps -a
# (venv) william@william-300E5M-300E5L:~/Documents/statistical-learning$ docker ps -a
# CONTAINER ID   IMAGE     COMMAND       CREATED        STATUS                    PORTS     NAMES
# 0267890844bb   ubuntu    "/bin/bash"   27 hours ago   Exited (0) 14 hours ago             webdev_study
# 0a792f11a2a8   ubuntu    "/bin/bash"   6 days ago     Exited (130) 6 days ago             go_study


docker run -p 3306:3306 --name mysql_study_dear -it ubuntu /bin/bash 
# My hypothesis is that we can access the mysql server from localhost

# (inside the container)
apt update
apt install mysql-server build-essential -y

service mysql status
service mysql start

# I would be easier to build a dockerfile for this
# instead of installing everything again
# but the main purpose of this is to learn and see the value of the
# dockerfile
# installing all by hand takes time

# using mysql shell
cd ~
/usr/bin/mysql -u root -p

ALTER USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY 'pass123';
exit;

mysql -u root -p
pass123

# create the database that we need
CREATE DATABASE stellar_classification;

# create new user
CREATE USER 'william'@'localhost' IDENTIFIED BY 'pass123';
GRANT ALL PRIVILEGES ON * . * TO 'william'@'localhost';
FLUSH PRIVILEGES;
exit;

mysql -u william -p
pass123

exit;

# exit the container
exit

# (in the host machine)
docker ps

docker start mysql_study_dear
docker exec mysql_study_dear service mysql start
docker exec mysql_study_dear service mysql status


# docker exec -it mysql_study_dear /bin/bash
# cd
# apt install build-essential -y



