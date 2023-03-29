docker run -d \
    -v /var/run/docker.sock:/var/run/docker.sock \
    --name study-container-airflow \
    -it ubuntu bash


docker run -d -v /var/run/docker.sock:/var/run/docker.sock --name study-container-airflow -it ubuntu bash

docker kill study-container-airflow
docker rm study-container-airflow

# ================================================================================ 
# Install inside the docker container
apt-get update &&
apt-get upgrade -y &&
apt-get install git build-essential curl wget unzip vim python3 python3-pip -y

# git config --global user.email "wllmszk@gmail.com" &&
# git config --global user.name "williamszk" &&
# git config pull.rebase false

# Install Docker
apt-get update
apt-get install \
    ca-certificates \
    curl \
    gnupg -y

mkdir -m 0755 -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  tee /etc/apt/sources.list.d/docker.list > /dev/null

apt-get update

apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

docker run hello-world

# ================================================================================ 
# https://www.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/learn/lecture/32289376#overview

curl -LO https://airflow.apache.org/docs/apache-airflow/2.5.1/docker-compose.yaml

docker compose up -d



