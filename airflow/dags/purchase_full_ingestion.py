from lakehouse_platform_core.airflow.ingestion_dag_builder import IngestionDagBuilder


CONFIG_PATH = "/opt/project/lakehouse-ingestion-engine/configs/ingestion/purchase/full.yaml"


dag = IngestionDagBuilder().build(CONFIG_PATH)