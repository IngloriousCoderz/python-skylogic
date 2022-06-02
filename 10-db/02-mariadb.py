# @see https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/

# Do another source .venv/bin/activate if mariadb is no resolved

import mariadb, sys

try:
  connection = mariadb.connect(
    user='root',
    password='burp',
    host='127.0.0.1',
    port=3306,
    database='skylogic'
  )
except mariadb.Error as error:
  print(f"Nope, {error}")
  sys.exit(1)

cursor = connection.cursor()

cursor.execute("CREATE TABLE tasks (title VARCHAR(255), is_done BOOL)")

values = [
  ('Learn Python', True),
  ('Look for a job', False),
  ('Forget everything', False)
]

cursor.executemany("INSERT INTO tasks VALUES (?, ?)", values)

connection.commit()

cursor.execute("SELECT * from tasks WHERE is_done = :is_done", {'is_done': True})

for (title, is_done) in cursor:
  print(f'Title: {title}, is_done: {is_done}')

connection.close()

# for OracleDB @see https://cx-oracle.readthedocs.io/en/latest/user_guide/installation.html#quick-start-cx-oracle-installation
