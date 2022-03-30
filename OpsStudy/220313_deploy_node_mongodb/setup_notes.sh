# The objective of this exercise is to set up a mongodb database in an EC2 instance
# then setup a nodejs server in another EC2 instance
# then we need to serve this application
# we want to practice creating and setting up the servers
# we are not interested in the DNS for now

# we'll create an EC2 instance

# verify if the ec2 instance have ssh allowed in the security group
# sgr-0290defa799001164	IPv4	SSH	TCP	22	0.0.0.0/0

# let's ssh into the mongodb ec2 instance
ssh -i "/root/statistical-learning/OpsStudy/samsungec2tutorial.pem" ec2-user@ec2-52-67-221-1.sa-east-1.compute.amazonaws.com
# got an error:
# Load key "/root/statistical-learning/OpsStudy/samsungec2tutorial.pem": bad permissions
# we need to change permissions of this key
# -rw-r--r--  1 root root 1700 Mar 13 17:10 samsungec2tutorial.pem
chmod 400 /root/statistical-learning/OpsStudy/samsungec2tutorial.pem
# -r--------  1 root root 1700 Mar 13 17:10 samsungec2tutorial.pem
# now it is just read, for the user

# run the ssh again
ssh -i "/root/statistical-learning/OpsStudy/samsungec2tutorial.pem" ec2-user@ec2-52-67-221-1.sa-east-1.compute.amazonaws.com
# root@17bd5980aa2c:~/statistical-learning/OpsStudy# ssh -i "/root/statistical-learning/OpsStudy/samsungec2tutorial.pem" ec2-user@ec2-52-67-221-1.sa-east-1.compute.amazonaws.com

#        __|  __|_  )
#        _|  (     /   Amazon Linux 2 AMI
#       ___|\___|___|

# https://aws.amazon.com/amazon-linux-2/
# No packages needed for security; 5 packages available
# Run "sudo yum update" to apply all updates.
# [ec2-user@ip-172-31-1-148 ~]$ 

# we are in the ec2 instance

# [inside the mongodb ec2 instance]

# we need to install mongodb in the ec2 instance

sudo yum update -y # update the pakcages

# https://docs.mongodb.com/manual/tutorial/install-mongodb-on-red-hat/
# we need to set configurations in yum so that we can install mongodb using yum
cd /etc/yum.repos.d
sudo touch mongodb-org-5.0.repo
ls
# [ec2-user@ip-172-31-1-148 yum.repos.d]$ ls
# amzn2-core.repo  amzn2-extras.repo  mongodb-org-5.0.repo
sudo vim mongodb-org-5.0.repo

# paste this into vim
# [mongodb-org-5.0]
# name=MongoDB Repository
# baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/5.0/x86_64/
# gpgcheck=1
# enabled=1
# gpgkey=https://www.mongodb.org/static/pgp/server-5.0.asc

sudo yum install -y mongodb-org

# got an error trying to install mongodb

# https://docs.mongodb.com/manual/tutorial/install-mongodb-on-amazon/
# I've found this tutorial specific for amazon distros

# verify linux distro
grep ^NAME /etc/*release
# [ec2-user@ip-172-31-1-148 yum.repos.d]$ grep ^NAME /etc/*release
# /etc/os-release:NAME="Amazon Linux"

# we need to paste this configuration into:
# /etc/yum.repos.d/mongodb-org-5.0.repo

# [mongodb-org-5.0]
# name=MongoDB Repository
# baseurl=https://repo.mongodb.org/yum/amazon/2/mongodb-org/5.0/x86_64/
# gpgcheck=1
# enabled=1
# gpgkey=https://www.mongodb.org/static/pgp/server-5.0.asc

sudo vim /etc/yum.repos.d/mongodb-org-5.0.repo
# it makes sense the name of the distro is different

sudo yum install -y mongodb-org
# now the installation is happening as expected

# Installed:
#   mongodb-org.x86_64 0:5.0.6-1.amzn2                                                                                                                                                         

# Dependency Installed:
#   cyrus-sasl.x86_64 0:2.1.26-24.amzn2          cyrus-sasl-gssapi.x86_64 0:2.1.26-24.amzn2               mongodb-database-tools.x86_64 0:100.5.2-1  mongodb-mongosh.x86_64 0:1.2.3-1.el8      
#   mongodb-org-database.x86_64 0:5.0.6-1.amzn2  mongodb-org-database-tools-extra.x86_64 0:5.0.6-1.amzn2  mongodb-org-mongos.x86_64 0:5.0.6-1.amzn2  mongodb-org-server.x86_64 0:5.0.6-1.amzn2 
#   mongodb-org-shell.x86_64 0:5.0.6-1.amzn2     mongodb-org-tools.x86_64 0:5.0.6-1.amzn2                

# Complete!

# start the mongodb service

# enter the ssh again
ssh -i "/root/statistical-learning/OpsStudy/samsungec2tutorial.pem" ec2-user@ec2-52-67-221-1.sa-east-1.compute.amazonaws.com

sudo systemctl start mongod
sudo systemctl status mongod

# [ec2-user@ip-172-31-1-148 ~]$ sudo systemctl status mongod
# ● mongod.service - MongoDB Database Server
#    Loaded: loaded (/usr/lib/systemd/system/mongod.service; enabled; vendor preset: disabled)
#    Active: active (running) since Sun 2022-03-13 21:08:39 UTC; 10s ago
#      Docs: https://docs.mongodb.org/manual
#   Process: 6944 ExecStart=/usr/bin/mongod $OPTIONS (code=exited, status=0/SUCCESS)
#   Process: 6941 ExecStartPre=/usr/bin/chmod 0755 /var/run/mongodb (code=exited, status=0/SUCCESS)
#   Process: 6938 ExecStartPre=/usr/bin/chown mongod:mongod /var/run/mongodb (code=exited, status=0/SUCCESS)
#   Process: 6937 ExecStartPre=/usr/bin/mkdir -p /var/run/mongodb (code=exited, status=0/SUCCESS)
#  Main PID: 6949 (mongod)
#    CGroup: /system.slice/mongod.service
#            └─6949 /usr/bin/mongod -f /etc/mongod.conf

# Mar 13 21:08:37 ip-172-31-1-148.sa-east-1.compute.internal systemd[1]: Starting MongoDB Database Server...
# Mar 13 21:08:38 ip-172-31-1-148.sa-east-1.compute.internal mongod[6944]: about to fork child process, waiting until server is ready for connections.
# Mar 13 21:08:38 ip-172-31-1-148.sa-east-1.compute.internal mongod[6944]: forked process: 6949
# Mar 13 21:08:39 ip-172-31-1-148.sa-east-1.compute.internal systemd[1]: Started MongoDB Database Server.

# experiment using the mongosh
mongosh

# [ec2-user@ip-172-31-1-148 ~]$ mongosh
# Current Mongosh Log ID: 622e5d9553e8862886cc66b1
# Connecting to:          mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.2.3
# Using MongoDB:          5.0.6
# Using Mongosh:          1.2.3

# For mongosh info see: https://docs.mongodb.com/mongodb-shell/


# To help improve our products, anonymous usage data is collected and sent to MongoDB periodically (https://www.mongodb.com/legal/privacy-policy).
# You can opt-out by running the disableTelemetry() command.

# ------
#    The server generated these startup warnings when booting:
#    2022-03-13T21:08:39.404+00:00: Access control is not enabled for the database. Read and write access to data and configuration is unrestricted
# ------

# test> 

# The installation of mongodb is complete

# ------------------------------------------------------------------- #

# let's set up another ec2 instance where we'll run the nodejs server

ssh -i "/root/statistical-learning/OpsStudy/samsungec2tutorial.pem" ec2-user@ec2-15-228-101-94.sa-east-1.compute.amazonaws.com

sudo yum update -y

# https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/setting-up-node-on-ec2-instance.html

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash

. ~/.nvm/nvm.sh

nvm install node

# [ec2-user@ip-172-31-4-236 ~]$ nvm install node
# Downloading and installing node v17.7.1...
# Downloading https://nodejs.org/dist/v17.7.1/node-v17.7.1-linux-x64.tar.xz...
# Computing checksum with sha256sum
# Checksums matched!
# Now using node v17.7.1 (npm v8.5.2)
# Creating default alias: default -> node (-> v17.7.1)


node -e "console.log('Running Node.js ' + process.version)"
# Running Node.js v17.7.1

# Finished installing nodejs

# gitclone the repo with the code for the application

# problem:
# [ec2-user@ip-172-31-4-236 ~]$ git
# -bash: git: command not found

sudo yum install git -y

git version
# [ec2-user@ip-172-31-4-236 ~]$ git version
# git version 2.32.0

git clone https://github.com/williamszk/webdev_study.git

ls
# [ec2-user@ip-172-31-4-236 ~]$ ls
# webdev_study

# the directory of the repo is there

cd ~/webdev_study/todolist-v3
ls
# [ec2-user@ip-172-31-4-236 todolist-v3]$ ls
# app.js  index.html  package.json  public  views

# install packages
npm i

node app.js

# [ec2-user@ip-172-31-4-236 todolist-v3]$ node app.js
# Server started on port 3000

# how to access the website from the browser?
# 15.228.101.94

# we need to allow inboud requests for https and http

# I think I need to install a webserver for outside requests
# for example we can use nginx or apache server or apache tomcat

# but I need to study how to do this...

# finish the study here






























