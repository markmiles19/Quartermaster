import sqlite3

DB_PATH = "data/sample.db"

# Forecasting seems to be working, but it's not yet clear if this one is.
def run_sql(query: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(query)
    results = cursor.fetchall()

    conn.close()
    return results