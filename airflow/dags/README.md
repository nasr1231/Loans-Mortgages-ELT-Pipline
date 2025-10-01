# 🚀 Custom Apache Airflow Image

This repository provides a custom **Apache Airflow 2.9.2 (Python 3.11)** Docker image with additional dependencies and system libraries required for running data engineering workflows.

---

## 🛠 Features
- Based on `apache/airflow:2.9.2-python3.11`
- Installs system dependencies:
  - `build-essential`, `gcc`
  - `libxml2-dev`, `libxslt1-dev`
  - `git`, `curl`
- Supports **PostgreSQL** connections via `psycopg2-binary`
- Environment management with **python-dotenv**
- Database ORM layer with **SQLAlchemy**

---

## 📋 Requirements
The image installs the following Python dependencies from `requirements.txt`:

- `sqlalchemy>=1.4.36,<2.0`
- `python-dotenv>=1.0.0`
- `psycopg2-binary>=2.9,<3.0`

## ⚡ Build the Image
Run the following command to build the custom Airflow image through your `docker-compose.yaml` file in Airflow Services (scheduler - webserver - init):

```bash
build:
    context: .
    dockerfile: Dockerfile