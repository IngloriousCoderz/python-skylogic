# @see https://docs.python.org/3/library/sqlite3.html

import sqlite3

# connection = sqlite3.connect("example.db") # creates the file
connection = sqlite3.connect(":memory:")

cursor = connection.cursor()

cursor.execute("CREATE TABLE tasks (text, is_done)")

values = [
  ('Learn Python', True),
  ('Look for a job', False),
  ('Forget everything', False)
]

cursor.executemany("INSERT INTO tasks VALUES (?, ?)", values)

connection.commit()

cursor.execute("SELECT * from tasks WHERE is_done = :is_done", {'is_done': True}) # you can use named args instead of positional

for (title, is_done) in cursor:
  print(f'Title: {title}, is_done: {is_done}')

connection.close()
