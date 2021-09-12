import csv
import psycopg2
import dotenv
import os
from collections import namedtuple
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
Stock = namedtuple(
    'Stock', 
    ['code', 'date', 'volume', 'open', 'high', 'low', 'close']
)
codes = [
    'ABCa', 'BNC', 'BOU', 'BPV', 'BVCC', 'BVL', 'CGQ', 'CIE', 'CRMa', 'DOM', 'EFE', 'ENV',
    'FVIa', 'FVIb', 'GZL'
]
rows_ves = []
rows_usd = []
for code in codes:
    with open(f'{BASE_DIR}\\stocks_usd_daily\\{code} Daily data_usd.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows_usd.append(
                Stock(
                    code=code,
                    date=row['Date'],
                    volume= int(float(row['Volumen'])),
                    open=float(row['Apertura Usd/Bs']),
                    high=float(row['Alto Usd/Bs']),
                    low=float(row['Bajo Usd/Bs']),
                    close=float(row['Cierre Usd/Bs']),
                )
            )
    with open(f'{BASE_DIR}\\stocks_ves_daily\\{code} Daily data.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows_ves.append(
                Stock(
                    code=code,
                    date=row['Date'],
                    volume= int(float(row['Volume'])),
                    open=float(row['Open']),
                    high=float(row['High']),
                    low=float(row['Low']),
                    close=float(row['Close']),
                )
            )

dotenv.read_dotenv()
conn = psycopg2.connect(
    database=os.environ.get('DATABASE_NAME'),
    password=os.environ.get('DATABASE_PASSWORD'),
    user=os.environ.get('DATABASE_USER'),
    host=os.environ.get('DATABASE_HOST'),
    port=os.environ.get('DATABASE_PORT')
)
cur = conn.cursor()

for row in rows:
    cur.execute(
        'INSERT INTO stock_ves (code, date, volume, open, high, low, close) VALUES (%s, %s, %s, %s, %s, %s, %s);', 
        (row.code, row.date, row.volume, row.open, row.high, row.low, row.close)
    )
        
for row in rows:
    cur.execute(
        'INSERT INTO stock_ves (code, date, volume, open, high, low, close) VALUES (%s, %s, %s, %s, %s, %s, %s);', 
        (row.code, row.date, row.volume, row.open, row.high, row.low, row.close)
    )

conn.commit()
cur.close()
conn.close()
print('All rows inserted')