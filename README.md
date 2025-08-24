# stock-data-pipeline-airflow
A Dockerized stock data pipeline using Apache Airflow and PostgreSQL
# Stock Data Pipeline with Apache Airflow

This project implements a Dockerized data pipeline using **Apache Airflow** to automatically fetch, parse, and store stock market data in a **PostgreSQL** database.

## 🚀 Features

- ⏱️ Scheduled data fetching (via Airflow DAG)
- 📈 Stock data fetched from a public API (e.g., Alpha Vantage)
- 🧩 JSON parsing & transformation
- 🗃️ Data storage in PostgreSQL
- 🐳 Fully containerized using Docker Compose
- ✅ Error handling and robustness built-in

## 🛠️ Tech Stack

- Apache Airflow (Scheduler + Webserver)
- PostgreSQL
- Docker + Docker Compose
- Python (`requests`, `psycopg2`)
- .env for secrets management

## 🔧 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/naveenkotnana/stock-data-pipeline-airflow.git
cd stock-data-pipeline-airflow
