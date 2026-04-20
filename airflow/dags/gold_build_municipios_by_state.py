from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="build_municipios_gold",
    start_date=datetime(2026, 4, 1),
    schedule=None,
    catchup=False,
    tags=["gold", "municipios", "lakehouse"],
) as dag:

    build_gold = BashOperator(
        task_id="build_municipios_by_state",
        bash_command="docker exec docker-spark-1 python /opt/project/src/gold/build_municipios_by_state.py",
    )

    build_gold