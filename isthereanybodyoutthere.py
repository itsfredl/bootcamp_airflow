from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dag_formation",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["pink"],
) as dag:
    un = BashOperator(
        task_id="un",
        bash_command="echo 1"
    )
    deux = BashOperator(
        task_id="deux",
        bash_command="echo 2"
    )
    trois = BashOperator(
        task_id="trois",
        bash_command="echo 3"
    )
    un >> [ deux, trois ]