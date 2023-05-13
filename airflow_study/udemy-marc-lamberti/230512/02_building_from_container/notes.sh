
# you need to be inside the same dir as the Dockerfile

# * Build a docker image from the Dockerfile in the current directory 
# (airflow-materials/airflow-basic)  and name it airflow-basic
docker build -t airflow-basic .

docker image ls

# create the container with everything that we need
docker run --rm -d -p 8080:8080 airflow-basic

