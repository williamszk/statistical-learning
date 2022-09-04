# let's use a EC2 instance to run the code related to this study
# https://www.udemy.com/course/docker-mastery/learn/lecture/6489842#overview
# docker study

ssh -i "~/Documents/aws_some_notes/thinkpadkeyec2tutorial.pem" ec2-user@ec2-15-229-18-239.sa-east-1.compute.amazonaws.com

# pem" ec2-user@ec2-15-229-18-239.sa-east-1.compute.amazonaws.com
# Last login: Fri Apr 22 14:12:46 2022 from 189.120.76.145

#        __|  __|_  )
#        _|  (     /   Amazon Linux 2 AMI
#       ___|\___|___|

# https://aws.amazon.com/amazon-linux-2/
# 28 package(s) needed for security, out of 53 available
# Run "sudo yum update" to apply all updates.
# [ec2-user@ip-172-31-34-236 ~]$ 


# nginx
docker version

# [ec2-user@ip-172-31-34-236 ~]$ docker version
# -bash: docker: command not found



# ----------------------------------------------------------------- #
# Which operating system?
# ----------------------------------------------------------------- #
# I think it is AWS Linux
cat /etc/os-release

# [ec2-user@ip-172-31-34-236 ~]$ cat /etc/os-release
# NAME="Amazon Linux"
# VERSION="2"
# ID="amzn"
# ID_LIKE="centos rhel fedora"
# VERSION_ID="2"
# PRETTY_NAME="Amazon Linux 2"
# ANSI_COLOR="0;33"
# CPE_NAME="cpe:2.3:o:amazon:amazon_linux:2"
# HOME_URL="https://amazonlinux.com/"


# ----------------------------------------------------------------- #
# How to install docker in Amazon Linux?
# ----------------------------------------------------------------- #

# https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-container-image.html

# Update the installed packages and package cache on your instance.
sudo yum update -y

# Install the most recent Docker Engine package.
sudo amazon-linux-extras install docker

# 

# Add the ec2-user to the docker group so you can execute Docker commands without using sudo.
sudo usermod -a -G docker ec2-user


docker info
# [ec2-user@ip-172-31-34-236 ~]$ docker info
# Client:
#  Context:    default
#  Debug Mode: false

# Server:
# ERROR: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
# errors pretty printing info

# The docker daemon is not running
systemctl start docker

docker version
# [ec2-user@ip-172-31-34-236 ~]$ docker version
# Client:
#  Version:           20.10.7
#  API version:       1.41
#  Go version:        go1.15.14
#  Git commit:        f0df350
#  Built:             Wed Nov 17 03:05:36 2021
#  OS/Arch:           linux/amd64
#  Context:           default
#  Experimental:      true
# Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?


# I need to log out and log in for the group change have effect
ssh -i "~/Documents/aws_some_notes/thinkpadkeyec2tutorial.pem" ec2-user@ec2-15-229-18-239.sa-east-1.compute.amazonaws.com

docker info
# [ec2-user@ip-172-31-34-236 ~]$ docker info
# Client:
#  Context:    default
#  Debug Mode: false

# Server:
# ERROR: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
# errors pretty printing info

# ERROR: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
# https://stackoverflow.com/questions/44678725/cannot-connect-to-the-docker-daemon-at-unix-var-run-docker-sock-is-the-docker

systemctl start docker
# [ec2-user@ip-172-31-34-236 ~]$ systemctl start docker
# Failed to start docker.service: The name org.freedesktop.PolicyKit1 was not provided by any .service files
# See system logs and 'systemctl status docker.service' for details.

# Failed to start docker.service: The name org.freedesktop.PolicyKit1 was not provided by any .service files
# https://stackoverflow.com/questions/39100641/docker-service-start-failed

dockerd
# [ec2-user@ip-172-31-34-236 ~]$ dockerd
# INFO[2022-04-22T14:27:02.596169123Z] Starting up                                  
# dockerd needs to be started with root. To see how to run dockerd in rootless mode with unprivileged user, see the documentation

sudo systemctl start docker
# this worked!
# it justed needed sudo

docker info
# [ec2-user@ip-172-31-34-236 ~]$ docker info
# Client:
#  Context:    default
#  Debug Mode: false

# Server:
#  Containers: 0
#   Running: 0
#   Paused: 0
#   Stopped: 0
#  Images: 0
#  Server Version: 20.10.7
#  Storage Driver: overlay2
#   Backing Filesystem: xfs
#   Supports d_type: true
#   Native Overlay Diff: true


# I'm using the Dockerfile to create a docker image
# create a directory for this experiment
mkdir 220422_01_dockerfile
cd 220422_01_dockerfile
touch Dockerfile
vim Dockerfile

# ----------------------------------------------------------------- #
# copy and paste the contents of the Dockerfile
# into the vim editor
# ----------------------------------------------------------------- #



# ----------------------------------------------------------------- #
# Let's build the Docker Image from the Dockerfile
# ----------------------------------------------------------------- #

docker build -t hello-world .
# I imagine that . means that the Dockerfile is in the same
# directory where this command is being ran

# [ec2-user@ip-172-31-34-236 220422_01_dockerfile]$ docker build -t hello-world .
# Sending build context to Docker daemon   2.56kB
# Step 1/6 : FROM ubuntu:18.04
# 18.04: Pulling from library/ubuntu
# 88736512a147: Pull complete 
# Digest: sha256:1c3f36f44928aafe1ae126b3e1bfe52d083f04bed7957012b3099e2176522c12
# Status: Downloaded newer image for ubuntu:18.04
#  ---> fdf0753c97a9
# Step 2/6 : RUN apt update && apt install apache2 -y
#  ---> Running in 700132e4a603

# WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

# . . . 

# Removing intermediate container 700132e4a603
#  ---> 04831d0582fd
# Step 3/6 : RUN echo "Hello World!" > /var/www/html/index.html
#  ---> Running in a233de0fe80a
# Removing intermediate container a233de0fe80a
#  ---> d25e5b3ede0f
# Step 4/6 : RUN echo ". /etc/apache2/envvars" > /root/run_apache.sh &&     echo "mkdir -p /var/run/apache2" >> /root/run_apache.sh &&     echo "mkdir -p /var/lock/apache2" >> /root/run_apache.sh &&     echo "/usr/sbin/apache2 -D FOREGROUND" >> /root/run_apache.sh &&     chmod 755 /root/run_apache.sh
#  ---> Running in f3a9a9c63a45
# Removing intermediate container f3a9a9c63a45
#  ---> b89a1d0a279a
# Step 5/6 : EXPOSE 80
#  ---> Running in 61769e40c568
# Removing intermediate container 61769e40c568
#  ---> 042b7255a70c
# Step 6/6 : CMD /root/run_apache.sh
#  ---> Running in 6dcea4b62408
# Removing intermediate container 6dcea4b62408
#  ---> 766599a0a6a8
# Successfully built 766599a0a6a8
# Successfully tagged hello-world:latest

# ----------------------------------------------------------------- #
# Run docker images to verify that the image was created correctly.
# ----------------------------------------------------------------- #

docker images --filter reference=hello-world
# [ec2-user@ip-172-31-34-236 220422_01_dockerfile]$ docker images --filter reference=hello-world
# REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
# hello-world   latest    766599a0a6a8   3 minutes ago   200MB

docker images
# [ec2-user@ip-172-31-34-236 220422_01_dockerfile]$ docker images
# REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
# hello-world   latest    766599a0a6a8   3 minutes ago   200MB
# ubuntu        18.04     fdf0753c97a9   16 hours ago    63.2MB

docker ps
# there is no containers running...


# ----------------------------------------------------------------- #
# Run the newly built image.
# ----------------------------------------------------------------- #

# The -p 80:80 option maps the exposed port 80 on the container 
# to port 80 on the host system.

docker run -t -i -p 80:80 hello-world
# [ec2-user@ip-172-31-34-236 220422_01_dockerfile]$ docker run -t -i -p 80:80 hello-world
# docker: Error response from daemon: driver failed programming external connectivity 
# on endpoint dazzling_almeida (f943259a0...): 
# Error starting userland proxy: listen tcp4 0.0.0.0:80: bind: address already in use.


# ----------------------------------------------------------------- #
# Error starting userland proxy: listen tcp4 0.0.0.0:80: bind: address already in use.
# ----------------------------------------------------------------- #

# https://stackoverflow.com/questions/37971961/docker-error-bind-address-already-in-use

# Using this in the browser:
# ec2-15-229-18-239.sa-east-1.compute.amazonaws.com
# shows the result from the Udemy AWS course by Stephane Marek
# I think that they are using apache
#

docker ps
# no container is running

# Maybe I can stop apache of the VM 
# and then I can expose the port 80 that the container will use


# ----------------------------------------------------------------- #
# how to see if apache is running?
# ----------------------------------------------------------------- #
# https://www.tecmint.com/check-apache-httpd-status-and-uptime-in-linux/

# for fedora and RHEL 
sudo systemctl status httpd

# [ec2-user@ip-172-31-34-236 220422_01_dockerfile]$ sudo systemctl status httpd
# ● httpd.service - The Apache HTTP Server
#    Loaded: loaded (/usr/lib/systemd/system/httpd.service; enabled; vendor preset: disabled)
#    Active: active (running) since sex 2022-04-22 14:20:51 UTC; 31min ago
#      Docs: man:httpd.service(8)
#  Main PID: 9882 (httpd)
#    Status: "Total requests: 2; Idle/Busy workers 100/0;Requests/sec: 0.00106; Bytes served/sec:   0 B/sec"
#     Tasks: 53
#    Memory: 1.2M
#    CGroup: /system.slice/httpd.service
#            ├─ 9882 /usr/sbin/httpd -DFOREGROUND
#            ├─ 9884 /usr/sbin/httpd -DFOREGROUND
#            ├─ 9885 /usr/sbin/httpd -DFOREGROUND
#            ├─ 9886 /usr/sbin/httpd -DFOREGROUND
#            ├─ 9887 /usr/sbin/httpd -DFOREGROUND
#            ├─ 9888 /usr/sbin/httpd -DFOREGROUND
#            └─11842 /usr/sbin/httpd -DFOREGROUND

# abr 22 14:20:51 ip-172-31-34-236.sa-east-1.compute.internal systemd[1]: Starting The Apache HTTP Server...
# abr 22 14:20:51 ip-172-31-34-236.sa-east-1.compute.internal systemd[1]: Started The Apache HTTP Server.

# Apache is running inside the VM

# Let's stop apache running from the VM
# so that we can use port 80 of the VM
# but the container will be using it.

sudo systemctl stop httpd
# this worked

# Check if Apache stoped
sudo systemctl status httpd
# [ec2-user@ip-172-31-34-236 220422_01_dockerfile]$ sudo systemctl status httpd
# ● httpd.service - The Apache HTTP Server
#    Loaded: loaded (/usr/lib/systemd/system/httpd.service; enabled; vendor preset: disabled)
#    Active: inactive (dead) since sex 2022-04-22 14:53:50 UTC; 25s ago
#      Docs: man:httpd.service(8)
#   Process: 9882 ExecStart=/usr/sbin/httpd $OPTIONS -DFOREGROUND (code=exited, status=0/SUCCESS)

# Apache is stopped

# ----------------------------------------------------------------- #
# Let's try again to run the container
# ----------------------------------------------------------------- #
docker run -t -i -p 80:80 hello-world

# [ec2-user@ip-172-31-34-236 220422_01_dockerfile]$ docker run -t -i -p 80:80 hello-world
# AH00558: apache2: Could not reliably determine the server's fully qualified domain name, 
# using 172.17.0.2. Set the 'ServerName' directive globally to suppress this message

# Apparently, it worked.

# Let's check using the browser to access the site:

# Write this in the browser:
# ec2-15-229-18-239.sa-east-1.compute.amazonaws.com
# It didn't work...
# It shows the same message as Stephane's course

# But I tried again and it worked.

# Maybe I needed to wait for cookies to wore off.
# Idk...

# But it shows the message "Hello World!"
# that we included in the Dockerfile

# Turn off the server
# And test again in the browser

# Now the site can't be reached
























