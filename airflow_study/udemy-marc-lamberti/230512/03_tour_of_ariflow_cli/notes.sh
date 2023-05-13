
# Quick Tour of Airflow CLI

docker ps
* Show running docker containers


docker exec -it container_id /bin/bash
* Execute the command /bin/bash in the container_id to get a shell session


pwd
* Print the current path where you are


airflow db init
* Initialise the metadatabase


airflow db reset
* Reinitialize the metadatabase (Drop everything)


airflow db upgrade
* Upgrade the metadatabase (Latest schemas, values, ...)


airflow webserver
* Start Airflow’s webserver


airflow scheduler
* Start Airflow’s scheduler


airflow celery worker
* Start a Celery worker (Useful in distributed mode to spread tasks among nodes - machines)


airflow dags list
* Give the list of known dags (either those in the examples folder or in dags folder)


ls
* Display the files/folders of the current directory 


airflow dags trigger example_python_operator
* Trigger the dag example_python_operator with the current date as execution date


airflow dags trigger example_python_operator -e 2021-01-01
* Trigger the dag example_python_operator with a date in the past as execution date (This won’t trigger the tasks of that dag unless you set the option catchup=True in the DAG definition)


airflow dags trigger example_python_operator -e '2021-01-01 19:04:00+00:00'
* Trigger the dag example_python_operator with a date in the future (change the date here with one having +2 minutes later than the current date displayed in the Airflow UI). The dag will be scheduled at that date.


airflow dags list-runs -d example_python_operator
* Display the history of example_python_operator’s dag runs


airflow tasks list example_python_operator
* List the tasks contained into the example_python_operator dag


airflow tasks test example_python_operator print_the_context 2021-01-01
* Allow to test a task (print_the_context) from a given dag (example_python_operator here) without taking care of dependencies and past runs. Useful for debugging.



