import sqlite3

conn = sqlite3.connect("data/sample.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS finances (
    id INTEGER PRIMARY KEY,
    balance REAL,
    daily_net REAL
)
""")

cursor.execute("""
INSERT INTO finances (balance, daily_net)
VALUES (5000, -150)
""")

conn.commit()
conn.close()