from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2025, 4, 7),
}

with DAG(
    dag_id='hello_steps',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    description='Argo-style steps: 'This is a simple hello world example using steps. hello1 -> [hello2a, hello2b]',
) as dag:

    hello1 = BashOperator(
        task_id='hello1',
        bash_command='echo "hello1"',
    )

    hello2a = BashOperator(
        task_id='hello2a',
        bash_command='echo "hello2a"',
    )

    hello2b = BashOperator(
        task_id='hello2b',
        bash_command='echo "hello2b"',
    )

    # Set dependencies
    hello1 >> [hello2a, hello2b]

