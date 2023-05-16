
python3 -m pip install --upgrade pip
pip install apache-airflow
pip install 'apache-airflow[postgres]'
pip install pandas


./start.sh


# to test the task that you created
docker exec -it <container id of airflow> bash
docker exec -it e6f5e935cc76 bash
# CONTAINER ID   IMAGE                   COMMAND                  CREATED          STATUS                    PORTS                                                      NAMES
# e6f5e935cc76   230515-airflow          "./entrypoint.sh ./s…"   12 minutes ago   Up 12 minutes (healthy)   0.0.0.0:8080->8080/tcp, :::8080->8080/tcp, 10000-10002/tcp


# list all dags
airflow dags list

# list the tasks of the dag of interest
airflow tasks list forex_data_pipeline

# test the new task by running it 
airflow tasks test forex_data_pipeline is_forex_available 2023-01-01
airflow tasks test forex_data_pipeline forex_file_sensor 2023-01-01

