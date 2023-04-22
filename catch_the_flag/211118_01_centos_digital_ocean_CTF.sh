# Digital Ocean
# droplet = VM instance
# 
# This project is being done using the job's laptop, the key is also in there.
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



# There's two tools that we think you'll find beneficial to hack on our labs but alternatives are readily available
# The following instructions and assuming you're installing these tools on an ubuntu/debian 
# based linux system although with a quick google search you'll find easy instalation instructions for other operating systems
# The two tools you'll be installing are ffuf and dnsecon

# ffuf
# dnsecon

# ffuf is a tool designed to rapidly automate web requests it can be used tasks such as discovering content, 
# directories, subdomains, virtual hosts, brute forcing account password and much more

# sudo add-apt-repository -y ppa:longsleep/golang-backports
# sudo apt update
# sudo apt install -y golang-go
# cd ~
# go get github.com/ffuf/ffuf
# sudo ln -s ~/go/bin/ffuf /usr/sbin/ffuf

# connect with digital ocean droplet
# 198.199.122.147
ssh -i "C:\Users\william.suzuki\.ssh\id_rsa" root@198.199.122.147
0

# -------------------------------------------------------------------------- #
# how to see centos version?
cat /etc/centos-release
# CentOS Linux release 8.5.2111

# https://www.cyberciti.biz/faq/how-to-install-wget-on-centos-8-using-the-yum-dnf-command/
sudo yum search wget
sudo yum install wget
wget --version

# install Go in centos
# https://linuxize.com/post/how-to-install-go-on-centos-7/
wget https://dl.google.com/go/go1.13.linux-amd64.tar.gz

sha256sum go1.13.linux-amd64.tar.gz

sudo tar -C /usr/local -xzf go1.13.linux-amd64.tar.gz

# include this line at .bash_profile
export PATH=$PATH:/usr/local/go/bin

# after including in the .bash_profile we need to run it
# $ source .bash_profile

# we need to install git
sudo yum search git
sudo yum install git

# we need to get ffuf software
go get github.com/ffuf/ffuf

# I think this function creates a symbolic link
sudo ln -s ~/go/bin/ffuf /usr/sbin/ffuf
# ln -s linux 
# https://geek-university.com/linux/symbolic-links/
# how to know if a file is a symbolic link?
# I think that the file has a turquoise color

# install dnsrecon
sudo yum search dnsrecon
# No matches found
# how to install dnsrecon in centos?


sudo yum search python
# how to install python in centos?
# https://linuxize.com/post/how-to-install-python-on-centos-8/
sudo dnf 

# centos have two package managers?
# dnf and yum
# is this correct?
# yes yum is a more recent package manager
sudo dnf install python3

# is dnsrecon in dnf?
sudo dnf search dnsrecon
# it is not in dnf

# Attribution link: https://latesthackingnews.com/2018/09/20/dnsrecon-an-open-source-dns-enumeration-tool
git clone https://github.com/darkoperator/dnsrecon
cd dnsrecon
pip3 install -r requirements.txt

# ./dnsrecon.py –d <target domain>
./dnsrecon.py -d google.com

# https://github.com/danielmiessler/SecLists

# about wordlist
mkdir wordlists
cd wordlists
wget https://ctfchallenge.com/wordlists-raw/content.txt
wget https://ctfchallenge.com/wordlists-raw/parameters.txt
wget https://ctfchallenge.com/wordlists-raw/passwords.txt
wget https://ctfchallenge.com/wordlists-raw/passwords-large.txt
wget https://ctfchallenge.com/wordlists-raw/subdomains.txt
wget https://ctfchallenge.com/wordlists-raw/usernames.txt


curl -H "Cookie: ctfchallenge=eyJkYXRhIjoiZXlKMWMyVnlYMmhoYzJnaU9pSjBZemQwZVc1NE5DSXNJbkJ5WlcxcGRXMGlPbVpoYkhObGZRPT0iLCJ2ZXJpZnkiOiJhYjUxMzhkMDBjM2M1Yjk1YzM0ZDgzMGU1YjdhNWZlYSJ9" http://challenge.test

ffuf -w ~/wordlists/content.txt -t 1 -p 0.1 -H "Cookie: ctfchallenge=eyJkYXRhIjoiZXlKMWMyVnlYMmhoYzJnaU9pSjBZemQwZVc1NE5DSXNJbkJ5WlcxcGRXMGlPbVpoYkhObGZRPT0iLCJ2ZXJpZnkiOiJhYjUxMzhkMDBjM2M1Yjk1YzM0ZDgzMGU1YjdhNWZlYSJ9" http://challenge.test/FUZZ
# -t number of threads
# -p rate per second
cat ~/wordlists/content.txt

nslookup -type=any vulnbegin.co.uk 8.8.8.8

ssh -i "C:\Users\william.suzuki\.ssh\id_rsa" root@198.199.122.147

./dnsrecon/dnsrecon.py -d vulnbegin.co.uk -D ~/wordlists/subdomains.txt -t brt
cat ~/wordlists/subdomains.txt

# server.vulnbegin.co.uk 139.59.177.128

curl -H "Cookie: ctfchallenge=eyJkYXRhIjoiZXlKMWMyVnlYMmhoYzJnaU9pSjBZemQwZVc1NE5DSXNJbkJ5WlcxcGRXMGlPbVpoYkhObGZRPT0iLCJ2ZXJpZnkiOiJhYjUxMzhkMDBjM2M1Yjk1YzM0ZDgzMGU1YjdhNWZlYSJ9" server.vulnbegin.co.uk

# what curl does?
# "Client URL"
# 













