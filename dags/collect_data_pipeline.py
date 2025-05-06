from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from shared.collect_data import DataCollector

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

with DAG(
    dag_id='collect_data_pipeline',
    default_args=default_args,
    description='A DAG to collect data from Binance',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',  # Or any cron expression
    catchup=False,
    tags=['trading', 'data_collection']
) as dag:

    def collect_data():
        collector = DataCollector(symbol='BTC/USDT', timeframe='5m', limit=1000, data_storage_name='btc_usdt_5m')
        collector.save_data()

    collect_data_task = PythonOperator(
        task_id='collect_data',
        python_callable=collect_data,
    )

    collect_data_task