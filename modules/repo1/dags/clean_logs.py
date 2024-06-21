from datetime import timedelta

import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator

raise Exception(str(__file__)+"||||"+str(__file__[:__file__.rfind("dags") + len("dags")]))
import sys
sys.path.insert(0,__file__[:__file__.rfind("dags") + len("dags")])

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
