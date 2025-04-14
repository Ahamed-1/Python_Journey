import sqlite3
from werkzeug.security import generate_password_hash

# Create database and table
conn = sqlite3.connect('./UAEP-IBM Project/users.db')
c = conn.cursor()

# Create users table
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              username TEXT UNIQUE,
              password TEXT)''')

# Predefined users
users = [
    ("Ahamed Basheer M", "Ahamed-1", "Ahamed@123"),
    ("Aishwarya DP", "DP-Ash", "Aishwarya@123"),
    ("Amreen Taj MA", "Amreen-Taj", "Amreen@123"),
    ("Lokesh M", "Loki-1", "Lokesh@123")
]

for name, username, password in users:
    hashed_pwd = generate_password_hash(password)
    c.execute("INSERT INTO users (name, username, password) VALUES (?, ?, ?)",
              (name, username, hashed_pwd))

conn.commit()
conn.close()