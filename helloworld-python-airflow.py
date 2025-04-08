from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
import random

# Function to generate a random integer
def generate_random_int():
    return random.randint(1, 100)

default_args = {
    'start_date': datetime(2025, 4, 7),
}

with DAG(
    dag_id='python_script_example',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    description='Python script example that generates and prints a random number.',
) as dag:

    # Task 1: Generate random integer
    generate = PythonOperator(
        task_id='generate_random_int',
        python_callable=generate_random_int,
    )

    # Task 2: Print message with the generated integer
    print_result = BashOperator(
        task_id='print_message',
        bash_command='echo "Result was: {{ task_instance.xcom_pull(task_ids="generate_random_int") }}"',
    )

    # Task dependencies
    generate >> print_result

