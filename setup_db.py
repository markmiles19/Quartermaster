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

# This will prevent any duplicates, just in case you did not follow the instructions in the README.
cursor.execute("DELETE FROM finances")

# This is essentially the database, at least before it gets inserted.
# Feel free to change the testing data as you please.
# Make sure it follows the (balance, daily_net) format.
data = [
    (12000, -500)
]

cursor.executemany("""
INSERT INTO finances (balance, daily_net)
VALUES (?, ?)
""", data)

conn.commit()
conn.close()