import sqlite3

DB_PATH = "data/sample.db"

def run_sql(query: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(query)
    results = cursor.fetchall()

    conn.close()
    return results