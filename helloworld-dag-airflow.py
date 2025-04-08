from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2025, 4, 7),
}

with DAG(
    dag_id='diamond_hello_world',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    description='Diamond DAG: B and C depend on A; D depends on both B and C.',
) as dag:

    task_a = BashOperator(
        task_id='A',
        bash_command='echo "A"',
    )

    task_b = BashOperator(
        task_id='B',
        bash_command='echo "B"',
    )

    task_c = BashOperator(
        task_id='C',
        bash_command='echo "C"',
    )

    task_d = BashOperator(
        task_id='D',
        bash_command='echo "D"',
    )

    # Define the diamond dependencies
    task_a >> [task_b, task_c]
    [task_b, task_c] >> task_d

