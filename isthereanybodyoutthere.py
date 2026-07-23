from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.trigger_rule import TriggerRule

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
        bash_command="echo 3",
        trigger_rule=TriggerRule.ONE_SUCCESS
    )
    quatre = BashOperator(
        task_id="quatre",
        bash_command="echo 4",
        trigger_rule=TriggerRule.ONE_FAILED
    )
    un >> [ trois, quatre ]