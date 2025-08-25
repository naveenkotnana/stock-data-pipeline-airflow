import os
import requests
import psycopg2
from dotenv import load_dotenv
import logging

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

API_KEY = os.getenv('60IV9QYQM144XISW')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

def fetch_stock_data(symbol="AAPL"):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={60IV9QYQM144XISW}'
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()
        if "Time Series (Daily)" not in data:
            raise ValueError(f"Missing 'Time Series (Daily)' in API response: {data}")
        return data["Time Series (Daily)"]
    except Exception as e:
        logging.error(f"Error fetching stock data: {e}")
        raise

def store_to_db(data, symbol="AAPL"):
    try:
        conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS)
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS stock_prices (
                symbol TEXT,
                date DATE,
                open FLOAT,
                high FLOAT,
                low FLOAT,
                close FLOAT,
                volume BIGINT,
                PRIMARY KEY (symbol, date)
            )
        """)
        for date, values in data.items():
            try:
                open_ = float(values.get('1. open', 0) or 0)
                high = float(values.get('2. high', 0) or 0)
                low = float(values.get('3. low', 0) or 0)
                close = float(values.get('4. close', 0) or 0)
                volume = int(values.get('5. volume', 0) or 0)
                cur.execute("""
                    INSERT INTO stock_prices (symbol, date, open, high, low, close, volume)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (symbol, date) DO UPDATE SET
                        open=EXCLUDED.open,
                        high=EXCLUDED.high,
                        low=EXCLUDED.low,
                        close=EXCLUDED.close,
                        volume=EXCLUDED.volume
                """, (
                    symbol, date, open_, high, low, close, volume
                ))
            except Exception as row_e:
                logging.warning(f"Skipping row for {date} due to error: {row_e}")
        conn.commit()
        cur.close()
        conn.close()
    except Exception as db_e:
        logging.error(f"Database error: {db_e}")
        raise

if __name__ == '__main__':
    try:
        stock_data = fetch_stock_data()
        store_to_db(stock_data)
        print("✅ Data successfully fetched and stored.")
    except Exception as e:
        print(f"❌ Error occurred: {e}")
