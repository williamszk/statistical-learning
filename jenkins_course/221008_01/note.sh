
# https://www.udemy.com/course/jenkins-from-zero-to-hero/learn/lecture/12847804#overview
mkdir jenkins-data

mkdir jenkins_home

# user 1000

# run the command below to see users
id
# uid=1000(william) gid=1000(william) groups=1000(william),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),121(lpadmin),132(lxd),133(sambashare),134(docker)

# spin up the container(s)
docker-compose up -d

# william@william-ThinkPad-T450:~/Documents/statistical-learning/jenkins_course/221008_01$ docker ps
# CONTAINER ID   IMAGE             COMMAND                  CREATED          STATUS         PORTS                                                  NAMES
# f5874b5d0d57   jenkins/jenkins   "/usr/bin/tini -- /u…"   15 seconds ago   Up 6 seconds   0.0.0.0:8080->8080/tcp, :::8080->8080/tcp, 50000/tcp   jenkins

# read the logs from the container
docker logs -f jenkins

# Jenkins initial setup is required. An admin user has been created and a password generated.
# Please use the following password to proceed to installation:

# 830e310b9c014a5bb395b8699d877399

# This may also be found at: /var/jenkins_home/secrets/initialAdminPassword

# We need to use this information
# In the browser we go to: localhost:8080
# there we need to use the token to confirm that we are the owners of the 
# jenkins server 

# ----------------------------------------------------
# Create first admin user
# william
# 830e310b9c014a5bb39

# another tutorial
# https://youtu.be/nCKxl7Q_20I?t=417


# ----------------------------------------------------
# stopped at:
# https://youtu.be/nCKxl7Q_20I?t=1927
# The video will enter in the part he works with Maven and Jenkins

# ----------------------------------------------------
# FullCycle Jenkins video
# https://www.youtube.com/watch?v=8OfhS5f7jIY&ab_channel=FullCycle

# just a checkpoint
# https://youtu.be/8OfhS5f7jIY?t=2177
# I had a problem with not having php and composer inside the container

# I need to install PHP inside the Jenkis server
# and then install Composer

# https://computingforgeeks.com/how-to-install-latest-php-on-debian/

# Step 1: Update system 
apt update && apt upgrade -y && reboot

# Step 2: Add SURY PHP PPA repository
apt -y install lsb-release apt-transport-https ca-certificates 
wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg
echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" | tee /etc/apt/sources.list.d/php.list

# Step 3: Install PHP 7.4 on Debian 10 / Debian 9
apt update
apt install php7.4 -y

# How to install Composer?
# https://www.hostinger.com/tutorials/how-to-install-composer
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"

# I have a problem with the container the default user is not root
# https://stackoverflow.com/a/72042637/15875971
docker exec -u 0 -it jenkins /bin/bash
# this works!
# we just need to include -u 0 

# try to run the job again

curl -sS https://getcomposer.org/installer | php
mv composer.phar /usr/bin/composer
# ----------------------------------------------------

