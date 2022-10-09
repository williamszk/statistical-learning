# https://www.youtube.com/watch?v=2PGnYjbYuUo&list=RDCMUCKXx22vOENUyHrVAADq7Z_g&start_radio=1&ab_channel=Geek%27sLesson

apt update
apt upgrade -y


# apt install ncal
# E: Unable to locate package ncal
# This is correct
apt install bsdmainutils

cal
#     August 2022       
# Su Mo Tu We Th Fr Sa  
#     1  2  3  4  5  6  
#  7  8  9 10 11 12 13  
# 14 15 16 17 18 19 20  
# 21 22 23 24 25 26 27  
# 28 29 30 31  
which cal
which ls


# cal: setlocale: No such file or directory
locale
# locale: Cannot set LC_CTYPE to default locale: No such file or directory
# locale: Cannot set LC_MESSAGES to default locale: No such file or directory
# locale: Cannot set LC_ALL to default locale: No such file or directory
# LANG=en_US.UTF-8
# LANGUAGE=
# LC_CTYPE="en_US.UTF-8"
# LC_NUMERIC="en_US.UTF-8"
# LC_TIME="en_US.UTF-8"
# LC_COLLATE="en_US.UTF-8"
# LC_MONETARY="en_US.UTF-8"
# LC_MESSAGES="en_US.UTF-8"
# LC_PAPER="en_US.UTF-8"
# LC_NAME="en_US.UTF-8"
# LC_ADDRESS="en_US.UTF-8"
# LC_TELEPHONE="en_US.UTF-8"
# LC_MEASUREMENT="en_US.UTF-8"
# LC_IDENTIFICATION="en_US.UTF-8"
# LC_ALL=

locale-gen "en_US.UTF-8"
# bash: locale-gen: command not found

apt install locales # <- this works
# there is no more warnings
locale-gen "en_US.UTF-8"

locale

cal
# root@a758414d3c9f:~/statistical-learning/bash_study# cal
#     August 2022       
# Su Mo Tu We Th Fr Sa  
#     1  2  3  4  5  6  
#  7  8  9 10 11 12 13  
# 14 15 16 17 18 19 20  
# 21 22 23 24 25 26 27  
# 28 29 30 31

# display current date and time
date
# root@a758414d3c9f:~/statistical-learning/bash_study# date
# Wed 03 Aug 2022 09:38:27 PM UTC

# print working directory
pwd
# root@a758414d3c9f:~/statistical-learning/bash_study# pwd
# /root/statistical-learning/bash_study

man pwd
# root@a758414d3c9f:~/statistical-learning/bash_study# man pwd
# This system has been minimized by removing packages and content that are
# not required on a system that users do not log into.

# To restore this content, including manpages, you can run the 'unminimize'
# command. You will still need to ensure the 'man-db' package is installed.

# I have this problem because I am using a container
apt install man-db

man pwd
# same problem

# It seems that this command is very impactful on the container
unminimize
# root@a758414d3c9f:~/statistical-learning/bash_study# unminimize
# This system has been minimized by removing packages and content that are
# not required on a system that users do not log into.

# This script restores content and packages that are found on a default
# Ubuntu server system in order to make this system more suitable for
# interactive use.

# Reinstallation of packages may fail due to changes to the system
# configuration, the presence of third-party packages, or for other
# reasons.

# This operation may take some time.

# Would you like to continue? [y/N] 

man pwd

echo "Hello World!"

# https://youtu.be/2PGnYjbYuUo?t=377