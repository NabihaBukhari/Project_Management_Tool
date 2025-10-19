import sqlite3

conn = sqlite3.connect('project.db')
cursor = conn.cursor()

print("\n--- USERS ---")
for row in cursor.execute("SELECT * FROM users"):
    print(row)

print("\n--- PROJECTS ---")
for row in cursor.execute("SELECT * FROM projects"):
    print(row)

print("\n--- TASKS ---")
for row in cursor.execute("SELECT * FROM tasks"):
    print(row)

conn.close()
