from datetime import timedelta

import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
# from src.handlers.log_handler import clean_logs

# from src.dags import Environment


def clean_logs(context):
    """Parse task context."""
    task = context["task_instance"]
    print(context["task_instance"])
    print(context["task_instance"].__dict__)
    print(context)

    return {
        "task_id": task.task_id,
        "log_url": task.log_url,
        "timestamp": str(context["execution_date"]),
    }
with DAG(
    dag_id="clean_logs",
    description="Clean log for a period",
    # schedule_interval=timedelta(days=float(Environment.LOG_DURATION)),
    start_date=pendulum.datetime(2022, 5, 24, tz="UTC"),
    end_date=None,
    catchup=False,
    tags=["airflow", "logs"],
) as dag:
    clean_logs_operator = PythonOperator(
        task_id="clean_logs", python_callable=lambda: None, 
        on_success_callback=clean_logs,
        on_failure_callback=clean_logs,
    )
    clean_logs_operator
    # Test commit 3
