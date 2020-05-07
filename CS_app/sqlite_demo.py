import sqlite3
from models import Employee

conn = sqlite3.connect('employee.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

#cursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, first TEXT, last TEXT)')

#cursor.execute('INSERT INTO users VALUES(?, ?, ?)', (1, 'Donald', 'Duck'))

#cursor.execute('INSERT INTO users(first, last) VALUES(?, ?)', ('Donald', 'Trump', ))

cursor.execute('SELECT * FROM users WHERE id=?', (1, ))
row = cursor.fetchone()

id = row[0]
first = row[1]
last = row[2]
print(str(id) + " " + first + " " + last)

e = Employee(first, last)
print(e)

