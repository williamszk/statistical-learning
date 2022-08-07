
https://www.udemy.com/course/data-engineering-essentials-sql-python-and-spark/learn/lecture/31004774#overview

https://github.com/itversity/data-engineering-spark


itvdflab -> jupyterlab

docker-compose build 

mkdir data-engineering-spark
cd data-engineering-spark
mkdir images
mkdir images/pythonsql
touch images/pythonsql/Dockerfile
touch images/pythonsql/labrequirements.txt
touch images/pythonsql/deploy.sh

mkdir ./cluster_util_db_scripts
mkdir ./itversity-material
mkdir ./data
mkdir ./cluster_util_db_scripts

docker network create itvdelabnw
docker network ls
# NETWORK ID     NAME               DRIVER    SCOPE
# a575e7819954   itvdelabnw         bridge    local

docker pull itversity/itvdelab
docker pull postgres:13

# experiment with this command
docker-compose build 

docker-compose up -d --build itvdflab
docker-compose ps

# Unsupported config option for services: 'itvdelab'
# Unsupported config option for networks: 'itvdelabnw'

git clone https://github.com/itversity/data-engineering-spark 
