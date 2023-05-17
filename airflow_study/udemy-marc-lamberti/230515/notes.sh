
python3 -m pip install --upgrade pip
pip install apache-airflow
pip install 'apache-airflow[postgres]'
pip install pandas
pip install requests
python3 -m pip install types-requests

# for hive
sudo apt-get install libsasl2-dev
pip install apache-airflow-providers-apache-hive

# for spark
pip install apache-airflow-providers-apache-spark

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

# test the new task downloading_rates
docker exec -it e6f5e935cc76 bash
airflow tasks test forex_data_pipeline downloading_rates 2023-01-01
# check the output of the task
cat /opt/airflow/dags/files/forex_rates.json

# test the new task "saving_rates"
docker exec -it 2b7821eb3861 bash
airflow tasks list forex_data_pipeline
airflow tasks test forex_data_pipeline saving_rates 2023-01-01

# test the new task "creating_forex_rates_table"
docker exec -it 2b7821eb3861 bash
airflow tasks list forex_data_pipeline
airflow tasks test forex_data_pipeline creating_forex_rates_table 2023-01-01












