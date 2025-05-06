from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from shared.clean_data import DataCleaning
from shared.feature_engineering import FeatureEngineering
from shared.train_model import TrainModel


default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

with DAG(
    dag_id='trading_model_pipeline',
    default_args=default_args,
    description='A DAG to clean, engineer features, and train trading model',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',  # Or any cron expression
    catchup=False,
    tags=['trading', 'ml']
) as dag:

    def clean_data():
        data_cleaner = DataCleaning()
        data_cleaner.clean_data()

    def feature_engineering():
        feature_engineer = FeatureEngineering()
        feature_engineer.feature_engineering()

    def train_model():
        model_trainer = TrainModel()
        model_trainer.train()

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