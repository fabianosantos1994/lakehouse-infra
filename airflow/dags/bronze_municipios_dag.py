from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


default_args = {
    "owner": "fabiano",
    "retries": 1,
}


with DAG(
    dag_id="bronze_municipios",
    default_args=default_args,
    start_date=datetime(2026, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    ingest_bronze = BashOperator(
        task_id="run_bronze_ingestion",
        bash_command="""
        docker exec docker-spark-1 \
            python /opt/project/src/bronze/ingest_municipios.py
            """,
    )

    ingest_bronze