from airflow import DAG, Dataset
from airflow.decorators import task

from datetime import datetime

my_file = Dataset("/tmp/my_file.txt")
my_file_2 = Dataset("/tmp/my_file_2.txt")

with DAG(
    dag_id="producer",
    schedule="@daily",
    start_date=datetime(2023, 5, 4),
    catchup=False,
):

    @task(outlets=[my_file])
    def update_dateset():
        with open(my_file.uri, "a+") as f:
            f.write("The producer is updating the Dataset my_file")

    @task(outlets=[my_file_2])
    def update_dateset_2():
        with open(my_file_2.uri, "a+") as f:
            f.write("The producer is updating the Dataset my_file_2")

    update_dateset() >> update_dateset_2()
