# 🏗️ Local Lakehouse Platform (V1)

## 📌 Overview

This project implements a local modern data platform based on a Lakehouse architecture.

It simulates a production-like environment using open-source technologies and follows the Medallion Architecture (Bronze, Silver, Gold).

## 🧠 Architecture

The platform is built with a clear separation of responsibilities:

* **MinIO** → Object Storage (S3-compatible)
* **Parquet** → File format
* **Apache Iceberg** → Table format
* **Hive Metastore** → Metadata catalog
* **PostgreSQL** → Backend for Hive Metastore and Airflow
* **Apache Spark** → Data processing engine
* **Apache Airflow** → Orchestration
* **Trino** → SQL query engine

### Compute Layer Separation

* **Spark** → ingestion and transformation
* **Trino** → query and analytics

## 🔄 Data Flow

```
Sources → Spark → Bronze → Silver → Gold → Trino → DBeaver
```

## 📦 Layers

* **Bronze** → raw ingestion
* **Silver** → cleaned and standardized data
* **Gold** → aggregated and business-ready datasets

## 🚀 Getting Started

### 1. Clone repository

```bash
git clone https://github.com/<your-user>/lakehouse-infra.git
cd lakehouse-infra/docker
```

### 2. Start infrastructure

```bash
docker compose up -d
```

### 3. Access services

* Airflow → http://localhost:8080
* Trino → http://localhost:8081
* MinIO → http://localhost:9001

## 🧪 Running Pipelines

Pipelines are orchestrated via Airflow.

Example DAGs:

* Bronze ingestion
* Silver transformation
* Gold aggregation

## 🔍 Querying Data

You can query data using:

* Trino CLI
* DBeaver

Example:

```sql
SELECT * FROM iceberg.gold.municipios_by_state;
```

## 📁 Repository Structure

```
docker/
trino/
airflow/
configs/
```

## 🎯 V1 Status

✅ Infrastructure ready
✅ Bronze pipeline
✅ Silver pipeline
✅ Gold pipeline
✅ Airflow orchestration
✅ Trino integration

## 🚀 Next Steps (V2)

* Dimensional modeling
* Data marts
* Business datasets

## Airflow DAG Registration Pattern

The local Airflow setup uses a simple and explicit DAG registration pattern for ingestion pipelines.

### Rule

- one ingestion YAML = one Airflow DAG
- one DAG registration file = one YAML pipeline

### DAG file location

Airflow DAG registration files must live in the Airflow DAG folder mounted by the local infrastructure.

Example:

```text
airflow/dags/purchase_full_ingestion.py
airflow/dags/crm_full_ingestion.py
```

## File naming convention

### Use the pattern:

```text
<source_database>_full_ingestion.py
```

Examples:

```text
purchase_full_ingestion.py
crm_full_ingestion.py
```

## DAG registration file content

Each file should remain minimal and only register the DAG for one YAML definition.

Example:

```python
from lakehouse_platform_core.airflow.ingestion_dag_builder import IngestionDagBuilder


CONFIG_PATH = "/opt/project/lakehouse-ingestion-engine/configs/ingestion/purchase/full.yaml"


dag = IngestionDagBuilder().build(CONFIG_PATH)
```

### Execution model

Airflow orchestrates execution only.

The actual ingestion processing runs inside the existing spark container through docker exec, using the runtime already validated for:

* PySpark
* PostgreSQL JDBC
* MinIO / S3A
* Iceberg

### Operational requirements

For DAG registration and execution to work correctly, the environment must provide:
* access to the DAG folder from Airflow
* access to lakehouse-platform-core
* access to lakehouse-ingestion-engine
* correct PYTHONPATH for Airflow imports
* Docker socket access for Airflow
* required environment variables available in the spark container

### Onboarding a new ingestion DAG

To register a new ingestion pipeline in Airflow:
1. create the YAML in lakehouse-ingestion-engine
2. ensure required environment variables exist in the spark container
3. create one DAG registration file in airflow/dags
4. point the file to the YAML path
5. confirm the DAG appears in the Airflow UI
6. execute and validate Bronze and Silver tasks