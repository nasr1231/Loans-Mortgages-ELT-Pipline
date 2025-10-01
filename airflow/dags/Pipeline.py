from airflow.decorators import dag, task
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
from jobs.tasks import *
import os
from dotenv import load_dotenv
import logging

load_dotenv("/opt/airflow/secrets.env")
    
def postgres_credentials():
    return {
        'host': os.getenv("POSTGRES_HOST"),
        'db_name': os.getenv("POSTGRES_DB"),
        'user': os.getenv("POSTGRES_USER"),
        'password': os.getenv("POSTGRES_PASSWORD"),
    }

# connection_string = f'postgresql://airflow:airflow@postgres/financial_data'

default_args = {
    "owner": "airflow-user",
    "retries": 2,
    "retry_delay": timedelta(minutes=1)
}

@dag(
    dag_id="Loan_ELT_Pipeline",
    start_date=datetime(2025, 9, 30),
    schedule_interval='@daily',
    catchup=False,
    default_args=default_args,
    tags=["Banking-ELT-Pipelines"]
)

def Loan_ELT_Pipeline():            
    
    @task()        
    def test_postgres_connection():        
        postgres_cred = postgres_credentials()
        conn, engine = postgres_connection(**postgres_cred)
        if conn is None or engine is None:
            logging.error("PostgreSQL connection has failed!")
            raise Exception("PostgreSQL connection could not be established.")
        
        logging.info("PostgreSQL connection has successfully established!")
        close_connection(conn, engine)
        
    data_ingestion_sqoop = BashOperator(
        task_id="data_ingestion_sqoop",
        bash_command="sqoop import --connect jdbc:postgresql://postgres:5432/financial_data --username airflow --password airflow --table financial_loan --target-dir hdfs://namenode:9000/staging-zone-5 --delete-target-dir"        
    )

    test_postgres_connection() >> data_ingestion_sqoop

Loan_ELT_Pipeline()