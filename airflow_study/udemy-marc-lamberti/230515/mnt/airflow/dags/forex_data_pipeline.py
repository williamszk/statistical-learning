import csv
import json
import requests
from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.http.sensors.http import HttpSensor
from airflow.sensors.filesystem import FileSensor
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.apache.hive.operators.hive import HiveOperator
from airflow.providers.apache.spark.operators.spark_submit import  SparkSubmitOperator
from airflow.operators.email import EmailOperator

default_args = {
    "owner": "airflow",
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "admin@localhost.com",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


def download_rates():
    BASE_URL = "https://gist.githubusercontent.com/marclamberti/f45f872dea4dfd3eaa015a4a1af4b39b/raw/"
    ENDPOINTS = {
        "USD": "api_forex_exchange_usd.json",
        "EUR": "api_forex_exchange_eur.json",
    }
    with open("/opt/airflow/dags/files/forex_currencies.csv") as forex_currencies:
        reader = csv.DictReader(forex_currencies, delimiter=";")
        for idx, row in enumerate(reader):
            base = row["base"]  # EUR, USD
            with_pairs = row["with_pairs"].split(" ")  # USD NZD JPY GBP CAD
            in_data = requests.get(f"{BASE_URL}{ENDPOINTS[base]}").json()
            out_data = {"base": base, "rates": {}, "last_update": in_data["date"]}
            for pair in with_pairs:
                out_data["rates"][pair] = in_data["rates"][pair]
            with open("/opt/airflow/dags/files/forex_rates.json", "a") as outfile:
                json.dump(out_data, outfile)
                outfile.write("\n")


with DAG(
    "forex_data_pipeline",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@daily",
    default_args=default_args,
    catchup=False,
) as dag:
    # For the connection:
    # conn id = forex_api
    # conn type = http
    # host = https://gist.github.com/
    is_forex_available = HttpSensor(
        task_id="is_forex_available",
        http_conn_id="forex_api",
        endpoint="marclamberti/f45f872dea4dfd3eaa015a4a1af4b39b",
        response_check=lambda response: "rates" in response.text,
        poke_interval=5,
        timeout=20,
    )

    # For the connection:
    # conn id = forex_path
    # conn type = file
    # Extra = {"path":"/opt/airflow/dags/files"}
    is_forex_currencies_file_available = FileSensor(
        task_id="is_forex_currencies_file_available",
        fs_conn_id="forex_path",
        filepath="forex_currencies.csv",
        poke_interval=5,
        timeout=20,
    )

    downloading_rates = PythonOperator(
        task_id="downloading_rates",
        python_callable=download_rates,
    )

    saving_rates = BashOperator(
        task_id="saving_rates",
        bash_command="""
            hdfs dfs -mkdir -p /forex && \
            hdfs dfs -put -f $AIRFLOW_HOME/dags/files/forex_rates.json /forex
        """,
    )

    # for the connection
    # Conn Id: hive_conn
    # Conn Type: Hive Server 2 Thrift
    # Host: hive-server
    # Login: hive
    # Password: hive
    # Port: 10000
    creating_forex_rates_table = HiveOperator(
        task_id="creating_forex_rates_table",
        hive_cli_conn_id="hive_conn",
        hql="""
            CREATE EXTERNAL TABLE IF NOT EXISTS forex_rates(
                base STRING,
                last_update DATE,
                eur DOUBLE,
                usd DOUBLE,
                nzd DOUBLE,
                gbp DOUBLE,
                jpy DOUBLE,
                cad DOUBLE
                )
            ROW FORMAT DELIMITED
            FIELDS TERMINATED BY ','
            STORED AS TEXTFILE
        """
    )

    # spark_submit
    # /opt/airflow/dags/scripts/forex_processing.py

    # Conn Id: spark_conn
    # Conn Type: Spark
    # Host: spark://spark-master
    # Port: 7077
    forex_processing = SparkSubmitOperator(
        task_id="forex_processing",
        application="/opt/airflow/dags/scripts/forex_processing.py",
        conn_id="spark_conn",
        verbose=False,
    )

    # https://security.google.com/settings/security/apppasswords
    send_email_notification = EmailOperator(
        task_id="send_email_notification",
        to="wllmszk@gmail.com",
        subject="forex_data_pipeline",
        html_content="<h3>forex_data_pipeline</h3>"
    )

