from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.trigger_rule import TriggerRule
from airflow.utils.task_group import TaskGroup
from airflow.models import Variable

test_variable=Variable.get("key_1")
with DAG(
    dag_id="dag_formation",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["pink"],
) as dag:

    with TaskGroup(group_id="groupe_1") as groupe_1:
        un = BashOperator(
            task_id="un",
            bash_command="echo 1; false"
            ti.xcom_pull(task_ids="groupe_1.un",value="foobar")
        )
        deux = BashOperator(
            task_id="deux",
            bash_command=f"echo '{test_variable}'",
            do_xcom_push=True
        )

    with TaskGroup(group_id="groupe_2") as groupe_2:
        trois = BashOperator(
            task_id="trois",
            bash_command="echo 3",
            trigger_rule=TriggerRule.ONE_SUCCESS
        )
        quatre = BashOperator(
            task_id="quatre",
            retval=it.xcom_pull(task_ids="groupe_1.un",key="foobar"),
            bash_command=f"echo {retval}",
            trigger_rule=TriggerRule.ONE_FAILED
        )

groupe_1 >> groupe_2