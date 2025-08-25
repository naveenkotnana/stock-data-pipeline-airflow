# Airflow DAG for Dockerized Stock Data Pipeline
"""
This DAG fetches stock data from Alpha Vantage API, parses it, and stores it in PostgreSQL.
Runs hourly. Robust error handling and environment variable management included.
"""

from airflow import DAG
from airflow.operators.bash import BashOperator  # For Airflow 2.x
from datetime import datetime, timedelta

with DAG(
    'stock_data_pipeline',
    default_args={
        'owner': 'airflow',
        'retries': 2,
        'retry_delay': timedelta(minutes=10),
    },
    description='Fetch, parse, and store stock data from API to PostgreSQL',
    schedule_interval='@hourly',
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:
    fetch_and_store = BashOperator(
        task_id='fetch_and_store',
        bash_command='python /opt/airflow/scripts/fetch_and_store.py',
        dag=dag,
    )
