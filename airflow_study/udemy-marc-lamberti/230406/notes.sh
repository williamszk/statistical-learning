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

# ================================================================================ 
# We should run this example using the hot machine so that we can use volumes
# I'm not sure if we can use volumes from one container to another container...

# I was using a strategy to use one container as the host machine, and spin up 
# other containers for testing if necessary.
# But this only works if I'm not using volumes.
# If I'm using volumes maybe we should just use the host machine.
#

# ================================================================================ 
# to test the connection
docker compose ps 
docker exec -it 220406-airflow-scheduler-1 bash

# inside the scheduler we can use the airflow cli
airflow -h

airflow tasks test <dag_id>        <task_id>    
airflow tasks test user_processing create_table 2023-04-05

# [2023-04-07 02:21:45,284] {dagbag.py:537} INFO - Filling up the DagBag from /opt/***/dags
# [2023-04-07 02:21:45,860] {taskmixin.py:205} WARNING - Dependency <Task(_PythonDecoratedOperator): print_the_context>, log_sql_query already registered for DAG: example_python_operator
# [2023-04-07 02:21:45,860] {taskmixin.py:205} WARNING - Dependency <Task(_PythonDecoratedOperator): log_sql_query>, print_the_context already registered for DAG: example_python_operator  
# [2023-04-07 02:21:45,861] {taskmixin.py:205} WARNING - Dependency <Task(_PythonDecoratedOperator): print_the_context>, log_sql_query already registered for DAG: example_python_operator
# [2023-04-07 02:21:45,861] {taskmixin.py:205} WARNING - Dependency <Task(_PythonDecoratedOperator): log_sql_query>, print_the_context already registered for DAG: example_python_operator  
# [2023-04-07 02:21:45,862] {taskmixin.py:205} WARNING - Dependency <Task(_PythonDecoratedOperator): print_the_context>, log_sql_query already registered for DAG: example_python_operator  
# [2023-04-07 02:21:45,862] {taskmixin.py:205} WARNING - Dependency <Task(_PythonDecoratedOperator): log_sql_query>, print_the_context already registered for DAG: example_python_operator  
# [2023-04-07 02:21:45,862] {taskmixin.py:205} WARNING - Dependency <Task(_PythonDecoratedOperator): print_the_context>, log_sql_query already registered for DAG: example_python_operator  
# [2023-04-07 02:21:45,863] {taskmixin.py:205} WARNING - Dependency <Task(_PythonDecoratedOperator): log_sql_query>, print_the_context already registered for DAG: example_python_operator  
# [2023-04-07 02:21:46,048] {taskmixin.py:205} WARNING - Dependency <Task(_PythonDecoratedOperator): prepare_email>, send_email already registered for DAG: example_dag_decorator
# [2023-04-07 02:21:46,048] {taskmixin.py:205} WARNING - Dependency <Task(EmailOperator): send_email>, prepare_email already registered for DAG: example_dag_decorator
# [2023-04-07 02:21:46,315] {taskmixin.py:205} WARNING - Dependency <Task(BashOperator): create_entry_group>, delete_entry_group already registered for DAG: example_complex
# [2023-04-07 02:21:46,316] {taskmixin.py:205} WARNING - Dependency <Task(BashOperator): delete_entry_group>, create_entry_group already registered for DAG: example_complex
# [2023-04-07 02:21:46,316] {taskmixin.py:205} WARNING - Dependency <Task(BashOperator): create_entry_gcs>, delete_entry already registered for DAG: example_complex
# [2023-04-07 02:21:46,316] {taskmixin.py:205} WARNING - Dependency <Task(BashOperator): delete_entry>, create_entry_gcs already registered for DAG: example_complex
# [2023-04-07 02:21:46,316] {taskmixin.py:205} WARNING - Dependency <Task(BashOperator): create_tag>, delete_tag already registered for DAG: example_complex
# [2023-04-07 02:21:46,316] {taskmixin.py:205} WARNING - Dependency <Task(BashOperator): delete_tag>, create_tag already registered for DAG: example_complex
# /home/airflow/.local/lib/python3.7/site-packages/airflow/cli/commands/task_command.py:133 RemovedInAirflow3Warning: Calling `DAG.create_dagrun()` without an explicit data interval is deprecated
# [2023-04-07 02:21:46,380] {taskinstance.py:1165} INFO - Dependencies all met for <TaskInstance: user_processing.create_table __***_temporary_run_2023-04-07T02:21:46.330858+00:00__ [None]>
# [2023-04-07 02:21:46,386] {taskinstance.py:1165} INFO - Dependencies all met for <TaskInstance: user_processing.create_table __***_temporary_run_2023-04-07T02:21:46.330858+00:00__ [None]>
# [2023-04-07 02:21:46,386] {taskinstance.py:1362} INFO -
# --------------------------------------------------------------------------------
# [2023-04-07 02:21:46,386] {taskinstance.py:1363} INFO - Starting attempt 1 of 1
# [2023-04-07 02:21:46,386] {taskinstance.py:1364} INFO -
# --------------------------------------------------------------------------------
# [2023-04-07 02:21:46,389] {taskinstance.py:1383} INFO - Executing <Task(PostgresOperator): create_table> on 2023-04-05T00:00:00+00:00
# [2023-04-07 02:21:46,565] {taskinstance.py:1592} INFO - Exporting the following env vars:
# AIRFLOW_CTX_DAG_OWNER=***
# AIRFLOW_CTX_DAG_ID=user_processing
# AIRFLOW_CTX_TASK_ID=create_table
# AIRFLOW_CTX_EXECUTION_DATE=2023-04-05T00:00:00+00:00
# AIRFLOW_CTX_TRY_NUMBER=1
# AIRFLOW_CTX_DAG_RUN_ID=__***_temporary_run_2023-04-07T02:21:46.330858+00:00__
# [2023-04-07 02:21:46,570] {base.py:71} INFO - Using connection ID 'postgres' for task execution.
# [2023-04-07 02:21:46,573] {sql.py:315} INFO - Running statement: --sql
#         CREATE TABLE IF NOT EXISTS users(
#             firstname TEXT NOT NULL,
#             lastname TEXT NOT NULL,
#             country TEXT NOT NULL,
#             username TEXT NOT NULL,
#             password TEXT NOT NULL,
#             email TEXT NOT NULL
#         );
#         , parameters: None
# [2023-04-07 02:21:46,585] {taskinstance.py:1406} INFO - Marking task as SUCCESS. dag_id=user_processing, task_id=create_table, execution_date=20230405T000000, start_date=, end_date=20230407T022146






