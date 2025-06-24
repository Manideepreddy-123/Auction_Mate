import sqlite3
from datetime import datetime, timedelta

with open("schema.sql") as f:
    sql = f.read()

conn = sqlite3.connect("database.db")
conn.executescript(sql)

# Insert sample product
now = datetime.now()
end_time = now + timedelta(hours=1)

conn.execute("INSERT INTO products (name, description, end_time) VALUES (?, ?, ?)",
             ("Smart Watch", "Stylish smart watch with health tracking", end_time.strftime("%Y-%m-%d %H:%M:%S")))
conn.commit()
conn.close()
