from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2025, 4, 7),
}

with DAG(
    dag_id='hello_world',
    default_args=default_args,
    schedule_interval=None,  # manual trigger
    catchup=False,
    description='This is a simple hello world example.',
) as dag:

    hello_world = BashOperator(
        task_id='print_hello',
        bash_command='echo "hello world"',
    )

