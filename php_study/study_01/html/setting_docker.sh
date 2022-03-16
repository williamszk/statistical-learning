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

# inside the the docker container:
apt update

apt install git -y

cd ~

git clone https://github.com/williamszk/statistical-learning.git

# this is a test inside the docker container

# I need to install mysql and php in the container
# https://linuxize.com/post/how-to-install-php-on-ubuntu-20-04/

# the author is using apache and mysql
apt install php libapache2-mod-php -y


# see if systemd exists
dpkg -l | grep systemd
apt install --reinstall systemd -y

# System has not been booted with systemd as init system (PID 1). Can't operate.
# Failed to connect to bus: Host is down
# example
# sudo service redis-server start

# see if apache2 is running
service apache2 status
# systemctl status apache2
# root@1e0366fd6f03:~/statistical-learning# service apache2 status
#  * apache2 is not running

service apache2 start
# systemctl restart apache2

# root@1e0366fd6f03:~/statistical-learning# service apache2 start
#  * Starting Apache httpd web server apache2                                                                                                                                            AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 172.17.0.2. Set the 'ServerName' directive globally to suppress this message
# AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 172.17.0.2. Set the 'ServerName' directive globally to suppress this message

# when we see the message above we go to:
# http://172.17.0.2/
# as specified in the messge
# we can find that the webserver is running
# http://172.17.0.2/phpmyadmin

service apache2 status
# root@1e0366fd6f03:~/statistical-learning# service apache2 status
#  * apache2 is running

php -v
# root@1e0366fd6f03:~/statistical-learning# php -v
# PHP 7.4.3 (cli) (built: Nov 25 2021 23:16:22) ( NTS )
# Copyright (c) The PHP Group
# Zend Engine v3.4.0, Copyright (c) Zend Technologies
#     with Zend OPcache v7.4.3, Copyright (c), by Zend Technologies

# we can see that php is installed


# https://github.com/thecodeholic/php-crash-course-2020


# how to make apache be able to access another directory besides /var/www/
ln -s /root/statistical-learning/php_study/html /var/www

# how to remove a symbolic link?
ls -la
# root@1e0366fd6f03:/var/www/php_study# ls -la
# total 8
# drwxr-xr-x 2 root root 4096 Jan 16 18:35 .
# drwxr-xr-x 4 root root 4096 Jan 16 18:35 ..
# lrwxrwxrwx 1 root root   36 Jan 16 18:35 php_study -> /root/statistical-learning/php_study

# l at the begining indicate it is a symbolic link

# https://linuxize.com/post/how-to-remove-symbolic-links-in-linux/
rm php_study

ls -la
# root@1e0366fd6f03:/var/www/php_study# ls -la
# total 8
# drwxr-xr-x 2 root root 4096 Jan 16 18:57 .
# drwxr-xr-x 4 root root 4096 Jan 16 18:35 ..

# Forbidden
# You don't have permission to access this resource.

# give permission to www-data which I imagine is the apache user to the directory
# that needs to be accessed
cd /root/statistical-learning/php_study/html
ls -l
# root@1e0366fd6f03:~/statistical-learning/php_study# ls -l
# total 4
# drwxr-xr-x 2 root root 4096 Jan 16 19:04 html

chown -R www-data:www-data /root/statistical-learning/php_study/html
# chown -R root:root /root/statistical-learning/php_study/html
ls -l
# root@1e0366fd6f03:~/statistical-learning/php_study# ls -l
# total 4
# drwxr-xr-x 2 www-data www-data 4096 Jan 16 19:04 html

chmod -R 0744 /root/statistical-learning/php_study/html

# https://stackoverflow.com/questions/22062266/how-to-give-apache-permission-to-write-to-home-directory/22062682
chmod -R 0777 /root/statistical-learning/php_study/html




