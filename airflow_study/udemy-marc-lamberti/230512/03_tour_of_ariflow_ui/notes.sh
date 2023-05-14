
# Quick Tour of Airflow CLI

# start the docker container (you need to be in the same dir as this file)
docker run --rm -d -p 8080:8080 --name airflow-container airflow-basic 

# * Show running docker containers
docker ps

# * Execute the command /bin/bash in the container_id to get a shell session
docker exec -it airflow-container /bin/bash

# * Print the current path where you are
pwd

