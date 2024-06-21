from datetime import timedelta

import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator

import os
import sys
dag_folder = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, dag_folder)

from dags.handlers.log_handler import clean_logs

from dags.config import Environment


with DAG(
    dag_id="clean_logs",
    description="Clean log for a period",
    schedule_interval=timedelta(days=float(Environment.LOG_DURATION)),
    start_date=pendulum.datetime(2022, 5, 24, tz="UTC"),
    end_date=None,
    catchup=False,
    tags=["airflow", "logs"],
) as dag:
    clean_logs_operator = PythonOperator(
        task_id="clean_logs", python_callable=clean_logs
    )
    clean_logs_operator
