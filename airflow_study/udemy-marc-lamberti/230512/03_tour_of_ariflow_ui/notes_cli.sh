
# About the Airflow CLI

# We need to use the notes.sh on this same directory to get into the docker
# container

airflow -h

# * Initialise the metadatabase
airflow db init

# * Reinitialize the metadatabase (Drop everything)
airflow db reset

# * Upgrade the metadatabase (Latest schemas, values, ...)
airflow db upgrade

# * Start Airflow’s webserver
airflow webserver

# * Start Airflow’s scheduler
airflow scheduler

# * Start a Celery worker (Useful in distributed mode to spread tasks among nodes - machines)
airflow celery worker

# * Give the list of known dags (either those in the examples folder or in dags folder)
airflow dags list

# * Display the files/folders of the current directory 
ls

# * Trigger the dag example_python_operator with the current date as execution date
airflow dags trigger example_python_operator

# * Trigger the dag example_python_operator with a date in the past as execution date (This won’t trigger the tasks of that dag unless you set the option catchup=True in the DAG definition)
airflow dags trigger example_python_operator -e 2021-01-01

# * Trigger the dag example_python_operator with a date in the future (change the date here with one having +2 minutes later than the current date displayed in the Airflow UI). The dag will be scheduled at that date.
airflow dags trigger example_python_operator -e '2021-01-01 19:04:00+00:00'

# * Display the history of example_python_operator’s dag runs
airflow dags list-runs -d example_python_operator
airflow dags list-runs -d example_bash_operator

# * List the tasks contained into the example_python_operator dag
airflow tasks list example_python_operator
airflow tasks list example_bash_operator

# * Allow to test a task (print_the_context) from a given dag (example_python_operator here) without taking care of dependencies and past runs. Useful for debugging.
# always after creating a new task inside a DAG test it by running this command
airflow tasks test example_python_operator print_the_context 2021-01-01
airflow tasks test example_bash_operator runme_0 2023-05-14

