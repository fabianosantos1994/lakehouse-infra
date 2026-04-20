from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


default_args = {
    "owner": "fabiano",
    "retries": 1,
}


with DAG(
    dag_id="municipios_pipeline",
    default_args=default_args,
    start_date=datetime(2026, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    bronze = BashOperator(
        task_id="run_bronze_ingestion",
        bash_command="""
        docker exec docker-spark-1 \
        python /opt/project/src/bronze/ingest_municipios.py
        """,
    )

    silver = BashOperator(
        task_id="run_silver_transformation",
        bash_command="""
        docker exec docker-spark-1 \
        python /opt/project/src/silver/silver_municipios.py
        """,
    )

    bronze >> silver