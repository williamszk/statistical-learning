# Digital Ocean
# droplet = VM instance
# 
# https://cloud.digitalocean.com/welcome?i=7605f9
# https://ctfchallenge.com/onboarding#

# ffuf is a tool designed to rapidly automate web requests it can be used tasks such as 
# discovering content, directories, subdomains, virtual hosts, brute forcing account password and much more

# this is a centos droplet in digital ocean
ssh -i "C:\Users\william.suzuki\.ssh\id_rsa" root@198.199.122.147

# how to update centos?
# https://www.cyberciti.biz/faq/centos-8-update-installed-packages-for-security/
# Show information about available update/packages,
sudo yum check-update

# to refresh package database and install updates.
sudo yum update

# how to see centos version?
cat /etc/centos-release
# CentOS Linux release 8.3.2011

# centos how to see system info?
# https://www.tecmint.com/commands-to-collect-system-and-hardware-information-in-linux/#:~:text=How%20to%20View%20Linux%20System,kernel%20name%20of%20your%20system.&text=To%20view%20your%20network%20hostname,the%20uname%20command%20as%20shown.
# How to View Linux System Hardware Information

# from CTF challenge, I need to install the following:

# $ sudo add-apt-repository -y ppa:longsleep/golang-backports
# $ sudo apt update
# $ sudo apt install -y golang-go
# $ cd ~
# $ go get github.com/ffuf/ffuf
# $ sudo ln -s ~/go/bin/ffuf /usr/sbin/ffuf


# github.com/ffuf/ffuf
# ffuf - Fuzz Faster U Fool
# visit the site

# how to install golang in centos?
# https://linuxize.com/post/how-to-install-go-on-centos-7/

# STOPED HERE!
# still needs to install golang























