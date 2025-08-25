# Dockerized Stock Data Pipeline (Airflow)

This project is a robust, Dockerized data pipeline that fetches, parses, and stores stock market data from a free API (Alpha Vantage) into PostgreSQL, orchestrated by Apache Airflow.

## Project Structure

```
stock_data_pipeline/
│
├── dags/
│   └── stock_pipeline.py            ← Airflow DAG (pipeline logic)
│
├── scripts/
│   └── fetch_and_store.py           ← Python script: fetch, parse, store
│
├── .env                             ← API keys and DB creds (not committed)
├── docker-compose.yml               ← Launch all services
├── Dockerfile                       ← Build image for custom Python dependencies
├── requirements.txt                 ← Python dependencies
└── README.md                        ← How to run & explain project
```

## Features & Requirements
- **Docker Compose**: One command to build and run the entire pipeline.
- **Airflow Orchestration**: Runs the pipeline hourly (can be changed in the DAG).
- **API Fetching**: Uses `requests` to get stock data from Alpha Vantage.
- **Data Extraction**: Parses JSON and extracts all relevant data points.
- **Database Update**: Updates/inserts into a PostgreSQL table.
- **Error Handling**: Robust try/except and missing data logic for resilience.
- **Security**: API keys and DB credentials managed via environment variables.
- **Scalability**: Easily extendable for more stocks, more frequent runs, or more tasks.

## Setup & Running

1. **Set up your environment variables:**
   - Copy `.env` and fill in your real API key and database credentials.

2. **Build and start the services:**
   ```sh
   docker-compose up --build
   ```

3. **Access Airflow UI:**
   - Go to [http://localhost:8080](http://localhost:8080)
   - Login (default: `airflow` / `airflow`)
   - Enable and trigger the `stock_data_pipeline` DAG
   - View logs for output and errors

4. **Database:**
   - PostgreSQL is available at `localhost:5432` with credentials from `.env`
   - Use DBeaver, pgAdmin, or `psql` to inspect the `stock_prices` table

## Deliverables
- `docker-compose.yml`: Compose file for all services
- `dags/stock_pipeline.py`: Airflow DAG (pipeline logic)
- `scripts/fetch_and_store.py`: Data fetching and DB update script
- `README.md`: This file

## Notes
- The Airflow DAG runs the pipeline hourly by default.
- Update the API endpoint, symbol, or DB logic in `fetch_and_store.py` as needed.
- `.env` should never be committed to version control.
