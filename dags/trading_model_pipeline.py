import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}
def clean_data():
    print("Cleaning data...")
def feature_engineering():
    print("feature_engineering data...")
def train_model():
    print("train_model data...")
with DAG(
    dag_id='trading_model_pipeline',
    default_args=default_args,
    description='A DAG to clean, engineer features, and train trading model',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',  # Or any cron expression
    catchup=False,
    tags=['trading', 'ml']
) as dag:

    clean_data_task = PythonOperator(
        task_id='clean_data',
        python_callable=clean_data,
    )

    feature_engineering_task = PythonOperator(
        task_id='feature_engineering',
        python_callable=feature_engineering,
    )

    train_model_task = PythonOperator(
        task_id='train_model',
        python_callable=train_model,
    )

    clean_data_task >> feature_engineering_task >> train_model_task