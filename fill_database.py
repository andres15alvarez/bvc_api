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
Usd = namedtuple('Usd', ['date', 'open', 'high', 'low', 'close'])
Ibc = namedtuple('Ibc', ['date', 'ibc'])
codes = [
    'ABCa', 'BNC', 'BOU', 'BPV', 'BVCC', 'BVL', 'CGQ', 'CIE', 'CRMa', 'DOM', 'EFE', 'ENV',
    'FVIa', 'FVIb', 'GZL'
]
rows_ves = []
rows_usd = []
rows_usd_exc = []
rows_ibc = []
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

with open(f'{BASE_DIR}\\data\\USD_BS.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows_usd_exc.append(
            Usd(
                date=row['Date'],
                open=float(row['Open']),
                high=float(row['High']),
                low=float(row['Low']),
                close=float(row['Price']),
            )
        )

with open(f'{BASE_DIR}\\data\\IBC.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        date = row['Date'].split('/')
        date = '-'.join([date[2], date[0], date[1]])
        rows_ibc.append(
            Ibc(
                date=date,
                ibc=row['IBC']
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

for row in rows_usd:
    cur.execute(
        'INSERT INTO stock_usd (code, date, volume, open, high, low, close) VALUES (%s, %s, %s, %s, %s, %s, %s);', 
        (row.code, row.date, row.volume, row.open, row.high, row.low, row.close)
    )
        
for row in rows_ves:
    cur.execute(
        'INSERT INTO stock_ves (code, date, volume, open, high, low, close) VALUES (%s, %s, %s, %s, %s, %s, %s);', 
        (row.code, row.date, row.volume, row.open, row.high, row.low, row.close)
    )

for row in rows_usd_exc:
    cur.execute(
            'INSERT INTO usd_exchange (date, open, high, low, close) VALUES (%s, %s, %s, %s, %s)',
            (row.date, row.open, row.high, row.low, row.close)
        )

for row in rows_ibc:
    cur.execute(
            'INSERT INTO ibc_ibc (date, ibc) VALUES (%s, %s)',
            (row.date, row.ibc)
        )

conn.commit()
cur.close()
conn.close()
print('All rows inserted')