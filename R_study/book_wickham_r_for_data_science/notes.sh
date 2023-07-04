
mkdir 230704

cd 230704

touch notes.sh

# ---------------------------------------------------------------------------
# how to install R
# how to install R in ubuntu?
# https://www.digitalocean.com/community/tutorials/how-to-install-r-on-ubuntu-22-04
wget -qO- https://cloud.r-project.org/bin/linux/ubuntu/marutter_pubkey.asc | sudo gpg --dearmor -o /usr/share/keyrings/r-project.gpg
echo "deb [signed-by=/usr/share/keyrings/r-project.gpg] https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/" | sudo tee -a /etc/apt/sources.list.d/r-project.list
sudo apt update
sudo apt install --no-install-recommends r-base

# To make the vscode R extension work


sudo apt install libxml2-dev
install.packages("xml2")
install.packages("languageserver")

# https://github.com/randy3k/radian
# install released version
pip3 install -U radian
# to run radian
radian

# Requirement already satisfied: radian in /home/ubuntu/.local/lib/python3.10/site-packages (0.6.6)
cd /home/ubuntu/.local/lib/python3.10/site-packages

# where is radian?
/home/ubuntu/.local/bin/radian

# this page helped me
# https://github.com/randy3k/radian/issues/372

# This article explains how to setup vscode to use R
# https://renkun.me/2019/12/11/writing-r-in-vscode-a-fresh-start/







