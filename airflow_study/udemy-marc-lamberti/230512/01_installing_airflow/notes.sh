# Installing airflow inside a container by hand
# instead of using a docker compose file

# --rm will delete the container after it is not used anymore
docker run -it --rm -p 8080:8080 python:3.8-slim /bin/bash

# installing airflow
export AIRFLOW_HOME=/usr/local/airflow

# * To check that the environment variable has been well exported
env | grep airflow

# * Install all tools and dependencies that can be required by Airflow
apt-get update -y && apt-get install -y wget libczmq-dev curl libssl-dev git inetutils-telnet bind9utils freetds-dev libkrb5-dev libsasl2-dev libffi-dev libpq-dev freetds-bin build-essential default-libmysqlclient-dev apt-utils rsync zip unzip gcc && apt-get clean

# * Create the user airflow, set its home directory to the value of 
# AIRFLOW_HOME and log into it
useradd -ms /bin/bash -d ${AIRFLOW_HOME} airflow

# * Show the file /etc/passwd to check that the airflow user has been 
# created
cat /etc/passwd | grep airflow

# * Upgrade pip (already installed since we use the Docker image python 3.5)
pip install --upgrade pip

# * Log into airflow
su - airflow

# * Create the virtual env named sandbox
python -m venv .sandbox

# * Activate the virtual environment sandbox
source .sandbox/bin/activate


# * Download the requirement file to install the right version of Airflow’s 
# dependencies 
wget https://raw.githubusercontent.com/apache/airflow/constraints-2.0.2/constraints-3.8.txt

# install airlfow with extras
# * Install the version 2.0.2 of apache-airflow with all subpackages 
# defined between square brackets. (Notice that you can still add 
# subpackages after all, you will use the same command with different 
# subpackages even if Airflow is already installed)
pip install "apache-airflow[crypto,celery,postgres,cncf.kubernetes,docker]"==2.0.2 --constraint ./constraints-3.8.txt

# * Initialise the metadatabase
airflow db init
ls airflow

# * Start Airflow’s scheduler in background
airflow scheduler &

# create a new airflow user
# run this before running the webserver
airflow users create -u admin -f admin \
    -l admin -r Admin -e admin@airflow.com -p admin 
# Admin user admin created

# * Start Airflow’s webserver in background
airflow webserver &

# =============================================================================
