# Lakehouse Infra

Local infrastructure for a Lakehouse-based data platform.

## Components

- MinIO
- PostgreSQL
- Hive Metastore
- Spark
- Iceberg

## Goal

Provide a local environment to support a modern data platform with decoupled storage, catalog, and processing layers.

## Current status

Validated locally:

- MinIO as object storage
- PostgreSQL as metastore backend
- Hive Metastore running with PostgreSQL
- Spark integrated with Iceberg
- Iceberg table creation and query working end-to-end

## Main folders

```text
docker/
  docker-compose.yml
  postgres/init/
  hive/conf/
  spark/conf/