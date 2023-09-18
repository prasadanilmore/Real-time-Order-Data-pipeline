from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import os

# Define DAG
dag = DAG(
    'order_data_pipeline',
    schedule_interval=None,  # Set your desired schedule
    start_date=datetime(2023, 9, 18),
    catchup=False,
    default_args={
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    },
)

# Define Python functions for tasks
def run_kafka_producer():
    os.system('python /kafka-producer/producer.py')

def run_spark_transform():
    os.system('spark-submit /spark-transform/transform.py')

# Define DAG tasks
start_task = DummyOperator(task_id='start', dag=dag)

kafka_producer_task = PythonOperator(
    task_id='run_kafka_producer',
    python_callable=run_kafka_producer,
    dag=dag,
)

spark_transform_task = PythonOperator(
    task_id='run_spark_transform',
    python_callable=run_spark_transform,
    dag=dag,
)

# Define task dependencies
start_task >> kafka_producer_task >> spark_transform_task
