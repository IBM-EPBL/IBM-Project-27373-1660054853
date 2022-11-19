import sqlite3

conn=sqlite3.connect("auth.db")
print("Database opended successfully")

conn.execute("Create Table table3 (name TEXT,mailid TEXT, password TEXT)")

print("created successfully")
conn.close()