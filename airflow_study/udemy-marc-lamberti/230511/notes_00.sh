
docker compose up -d

# If building a new virtual environment:
python -m pip install --upgrade pip
pip install apache-airflow
pip install 'apache-airflow[postgres]'
pip install pandas


# How to test an individual task?
docker exec -it 230424-airflow-scheduler-1 bash
# [ inside scheduler ]

# check help of airflow cli
airflow -h

# start a task from a dag
# airflow tasks test <dag_id>        <task_id>    
airflow tasks test user_processing create_table 2023-04-20
# it worked

airflow tasks test user_processing is_api_available 2023-04-20
# it worked, but in the test connection it didn't work...


# ============================================================================
# Check the file /tmp/processed_user.csv inside the worker container
docker ps -a
docker exec -it 230424-airflow-worker-1 bash
cd /tmp/

# ============================================================================
# Check the contents of the postgres database
docker exec -it 230424-postgres-1 bash
psql -U airflow -W -h localhost

# [ inside the psql ]
# show tables
\dt

\dt users

select * from users;