from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2025, 4, 7),
}

with DAG(
    dag_id='hello_world_scheduled',
    default_args=default_args,
    schedule_interval='* * * * *',  # Run every minute
    catchup=False,
    description='This is a simple hello world example using cron.',
) as dag:

    print_hello = BashOperator(
        task_id='print_hello',
        bash_command='echo "hello world $(date)"',
    )

