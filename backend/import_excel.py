import pandas as pd
import sqlite3

df = pd.read_excel('../data/0904.xlsm.xlsx', sheet_name='BD')

conn = sqlite3.connect('../backend/db.sqlite3')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS producao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT NOT NULL,
    unidade TEXT NOT NULL,
    meta REAL NOT NULL,
    realizado REAL NOT NULL
)''')

for _, row in df.iterrows():
    cursor.execute('''
        INSERT INTO producao (data, unidade, meta, realizado)
        VALUES (?, ?, ?, ?)''',
        (row['Data'], row['Unidade'], row['Meta'], row['Realizado']))

conn.commit()
conn.close()
