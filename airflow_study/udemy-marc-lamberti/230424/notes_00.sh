docker compose up -d

# If building a new virtual environment:
python.exe -m pip install --upgrade pip
pip install apache-airflow
pip install 'apache-airflow[postgres]'
pip install pandas

# Remeber that we need to connect the airflow with the postgres database
# https://www.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/learn/lecture/32340586#overview

# ================================================================================ 
# https://www.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/learn/lecture/32289376#overview

curl -LO https://airflow.apache.org/docs/apache-airflow/2.5.1/docker-compose.yaml

docker compose up -d

# ================================================================================ 
# We should run this example using the host machine so that we can use volumes
# I'm not sure if we can use volumes from one container to another container...

# I was using a strategy to use one container as the host machine, and spin up 
# other containers for testing if necessary.
# But this only works if I'm not using volumes.
# If I'm using volumes maybe we should just use the host machine.

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

# ==============================================================================
# To go inside the postgres database and take a look what is inside there
psql -U airflow -W -h localhost

# show tables
\dt
#                      List of relations
#  Schema |              Name              | Type  |  Owner
# --------+--------------------------------+-------+---------
#  public | ab_permission                  | table | airflow
#  public | ab_permission_view             | table | airflow
#  public | ab_permission_view_role        | table | airflow
#  public | ab_register_user               | table | airflow
#  public | ab_role                        | table | airflow
#  public | ab_user                        | table | airflow
#  public | ab_user_role                   | table | airflow
#  public | ab_view_menu                   | table | airflow
#  public | alembic_version                | table | airflow
#  public | callback_request               | table | airflow
#  public | celery_taskmeta                | table | airflow
#  public | celery_tasksetmeta             | table | airflow
#  public | connection                     | table | airflow
#  public | dag                            | table | airflow
#  public | dag_code                       | table | airflow
#  public | dag_owner_attributes           | table | airflow
#  public | dag_pickle                     | table | airflow
#  public | dag_run                        | table | airflow
#  public | dag_schedule_dataset_reference | table | airflow
#  public | dag_tag                        | table | airflow
#  public | dag_warning                    | table | airflow
#  public | dagrun_dataset_event           | table | airflow
#  public | dataset                        | table | airflow
#  public | dataset_dag_run_queue          | table | airflow
#  public | dataset_event                  | table | airflow
#  public | import_error                   | table | airflow
#  public | job                            | table | airflow
#  public | log                            | table | airflow
#  public | log_template                   | table | airflow
#  public | rendered_task_instance_fields  | table | airflow
#  public | serialized_dag                 | table | airflow
#  public | session                        | table | airflow
#  public | sla_miss                       | table | airflow
#  public | slot_pool                      | table | airflow
#  public | task_fail                      | table | airflow
#  public | task_instance                  | table | airflow
#  public | task_map                       | table | airflow
#  public | task_outlet_dataset_reference  | table | airflow
#  public | task_reschedule                | table | airflow
#  public | trigger                        | table | airflow
#  public | users                          | table | airflow <-- here is the table
#  public | variable                       | table | airflow
#  public | xcom                           | table | airflow
# (43 rows)

\dt users
# airflow=# \dt users
#         List of relations
#  Schema | Name  | Type  |  Owner
# --------+-------+-------+---------
#  public | users | table | airflow
# (1 row)


# ==============================================================================
# How to test your new tasks
# execute task in the airflow cli
docker exec -it <id of the scheduler container> bash
docker exec -it 230406-airflow-scheduler-1 bash
# [inside the container]
airflow tasks test <id of dag> <id of task> <a date in the past>
airflow tasks test user_processing create_table 2023-04-20
# [2023-04-23 20:22:00,673] {taskinstance.py:1165} INFO - Dependencies all met for <TaskInstance: user_processing.create_table __***_temporary_run_2023-04-23T20:22:00.630855+00:00__ [None]>
# [2023-04-23 20:22:00,679] {taskinstance.py:1165} INFO - Dependencies all met for <TaskInstance: user_processing.create_table __***_temporary_run_2023-04-23T20:22:00.630855+00:00__ [None]>
# [2023-04-23 20:22:00,680] {taskinstance.py:1362} INFO -
# --------------------------------------------------------------------------------
# [2023-04-23 20:22:00,680] {taskinstance.py:1363} INFO - Starting attempt 1 of 1
# [2023-04-23 20:22:00,680] {taskinstance.py:1364} INFO -
# --------------------------------------------------------------------------------
# [2023-04-23 20:22:00,683] {taskinstance.py:1383} INFO - Executing <Task(PostgresOperator): create_table> on 2023-04-20T00:00:00+00:00
# [2023-04-23 20:22:00,883] {taskinstance.py:1592} INFO - Exporting the following env vars:
# AIRFLOW_CTX_DAG_OWNER=***
# AIRFLOW_CTX_DAG_ID=user_processing
# AIRFLOW_CTX_TASK_ID=create_table
# AIRFLOW_CTX_EXECUTION_DATE=2023-04-20T00:00:00+00:00
# AIRFLOW_CTX_TRY_NUMBER=1
# AIRFLOW_CTX_DAG_RUN_ID=__***_temporary_run_2023-04-23T20:22:00.630855+00:00__
# [2023-04-23 20:22:00,888] {base.py:71} INFO - Using connection ID 'my_postgres_conn_id' for task execution.    
# [2023-04-23 20:22:00,891] {sql.py:315} INFO - Running statement: --sql
#         CREATE TABLE IF NOT EXISTS users(
#             firstname TEXT NOT NULL,
#             lastname TEXT NOT NULL,
#             country TEXT NOT NULL,
#             username TEXT NOT NULL,
#             password TEXT NOT NULL,
#             email TEXT NOT NULL
#         );
#         , parameters: None
# [2023-04-23 20:22:00,892] {postgres.py:96} INFO - NOTICE:  relation "users" already exists, skipping

# [2023-04-23 20:22:00,892] {taskinstance.py:1406} INFO - Marking task as SUCCESS. dag_id=user_processing, task_id=create_table, execution_date=20230420T000000, start_date=, end_date=20230423T202200

# check if the is_api_available task is running ok...
docker exec -it 230406-airflow-scheduler-1 bash
airflow tasks test user_processing is_api_available 2023-04-20
# [2023-04-23 20:49:18,353] {taskinstance.py:1165} INFO - Dependencies all met for <TaskInstance: user_processing.is_api_available __***_temporary_run_2023-04-23T20:49:18.313524+00:00__ [None]>
# [2023-04-23 20:49:18,359] {taskinstance.py:1165} INFO - Dependencies all met for <TaskInstance: user_processing.is_api_available __***_temporary_run_2023-04-23T20:49:18.313524+00:00__ [None]>
# [2023-04-23 20:49:18,360] {taskinstance.py:1362} INFO - 
# --------------------------------------------------------------------------------
# [2023-04-23 20:49:18,360] {taskinstance.py:1363} INFO - Starting attempt 1 of 1
# [2023-04-23 20:49:18,360] {taskinstance.py:1364} INFO - 
# --------------------------------------------------------------------------------
# [2023-04-23 20:49:18,363] {taskinstance.py:1383} INFO - Executing <Task(HttpSensor): is_api_available> on 2023-04-20T00:00:00+00:00
# [2023-04-23 20:49:18,538] {taskinstance.py:1592} INFO - Exporting the following env vars:
# AIRFLOW_CTX_DAG_OWNER=***
# AIRFLOW_CTX_DAG_ID=user_processing
# AIRFLOW_CTX_TASK_ID=is_api_available
# AIRFLOW_CTX_EXECUTION_DATE=2023-04-20T00:00:00+00:00
# AIRFLOW_CTX_TRY_NUMBER=1
# AIRFLOW_CTX_DAG_RUN_ID=__***_temporary_run_2023-04-23T20:49:18.313524+00:00__
# [2023-04-23 20:49:18,539] {http.py:120} INFO - Poking: api/
# [2023-04-23 20:49:18,543] {base.py:71} INFO - Using connection ID 'user_api' for task execution.
# [2023-04-23 20:49:18,544] {http.py:148} INFO - Sending 'GET' to url: https://randomuser.me/api/ 
# [2023-04-23 20:49:18,895] {base.py:213} INFO - Success criteria met. Exiting.
# [2023-04-23 20:49:18,896] {taskinstance.py:1406} INFO - Marking task as SUCCESS. dag_id=user_processing, task_id=is_api_available, execution_date=20230420T000000, start_date=, end_date=20230423T204918
# airflow@eed7ba10a5c1:/opt/airflow$ 

# ==============================================================================
# How to make connection for postgres


# How to make connection for http for https://randomuser.me/

# ==============================================================================
