import time
import sqlite3
from models import User, GList, Item

conn = sqlite3.connect('Wasteapp.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

#cursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, first TEXT, last TEXT)')

#cursor.execute('INSERT INTO users VALUES(?, ?, ?)', (1, 'Donald', 'Duck'))

#cursor.execute('INSERT INTO users(first, last) VALUES(?, ?)', ('Donald', 'Trump', ))

#cursor.execute('SELECT * FROM users WHERE id=?', (1, ))
#row = cursor.fetchone()

'''
id = row[0]
first = row[1]
last = row[2]
print(str(id) + " " + first + " " + last)

e = Employee(first, last)
print(e)
'''

'''
cursor.execute('DROP TABLE User')
cursor.execute('DROP TABLE GList')
cursor.execute('DROP TABLE Item')

cursor.execute('CREATE TABLE User (id INTEGER PRIMARY KEY, name TEXT, password TEXT)')
cursor.execute('CREATE TABLE Glist (id INTEGER PRIMARY KEY, userid TEXT, name TEXT, FOREIGN KEY (userid) REFERENCES Users (id) ON DELETE CASCADE )')
cursor.execute('CREATE TABLE Item (id INTEGER PRIMARY KEY, glistid TEXT, name TEXT, cals INTEGER, exp_date TEXT, FOREIGN KEY (glistid) REFERENCES Glist (id) ON DELETE CASCADE )')

cursor.execute('INSERT INTO User(name, password) VALUES(?, ?)', ('Marcel', '123456', ))
cursor.execute('INSERT INTO User(name, password) VALUES(?, ?)', ('Ionut', 'asdfgh', ))
cursor.execute('INSERT INTO GList(userid, name) VALUES(?, ?)', (1, 'List1', ))
cursor.execute('INSERT INTO GList(userid, name) VALUES(?, ?)', (1, 'List2', ))
cursor.execute('INSERT INTO GList(userid, name) VALUES(?, ?)', (2, 'List1', ))
cursor.execute('INSERT INTO GList(userid, name) VALUES(?, ?)', (2, 'List2', ))
cursor.execute('INSERT INTO GList(userid, name) VALUES(?, ?)', (2, 'List3', ))
cursor.execute('INSERT INTO Item(glistid, name, cals, exp_date) VALUES(?, ?, ?, ?)', (1, 'cheese', 10, '2020-05-08'))
cursor.execute('INSERT INTO Item(glistid, name, cals, exp_date) VALUES(?, ?, ?, ?)', (1, 'chocolate', 64, '2020-05-09'))
cursor.execute('INSERT INTO Item(glistid, name, cals, exp_date) VALUES(?, ?, ?, ?)', (2, 'bread', 23, '2020-05-10'))
cursor.execute('INSERT INTO Item(glistid, name, cals, exp_date) VALUES(?, ?, ?, ?)', (2, 'milk', 45, '2020-05-11'))
cursor.execute('INSERT INTO Item(glistid, name, cals, exp_date) VALUES(?, ?, ?, ?)', (3, 'eggs', 54, '2020-05-12'))
cursor.execute('INSERT INTO Item(glistid, name, cals, exp_date) VALUES(?, ?, ?, ?)', (3, 'flour', 23, '2020-05-13'))
cursor.execute('INSERT INTO Item(glistid, name, cals, exp_date) VALUES(?, ?, ?, ?)', (4, 'candies', 74, '2020-05-14'))
cursor.execute('INSERT INTO Item(glistid, name, cals, exp_date) VALUES(?, ?, ?, ?)', (4, 'orange juice', 54, '2020-05-15'))
cursor.execute('INSERT INTO Item(glistid, name, cals, exp_date) VALUES(?, ?, ?, ?)', (4, 'orange', 45, '2020-05-16'))
cursor.execute('INSERT INTO Item(glistid, name, cals, exp_date) VALUES(?, ?, ?, ?)', (5, 'bananas', 12, '2020-05-17'))
cursor.execute('INSERT INTO Item(glistid, name, cals, exp_date) VALUES(?, ?, ?, ?)', (5, 'tomatoes', 30, '2020-05-18'))
cursor.execute('INSERT INTO Item(glistid, name, cals, exp_date) VALUES(?, ?, ?, ?)', (5, 'cucumbers', 20, '2020-01-19'))
conn.commit()
'''

def insertUser(name, password):
	cursor.execute('INSERT INTO User(name, password) VALUES(?, ?)', (name, password, ))
	conn.commit()

def insertGList(userid, name):
	cursor.execute('INSERT INTO GList(userid, name) VALUES(?, ?)', (userid, name, ))
	conn.commit()

def insertItem(glistid, name, cals, exp_date):
	cursor.execute('INSERT INTO Item(glistid, name, cals, exp_date) VALUES(?, ?, ?, ?)', (glistid, name, int(cals), str(exp_date)))
	conn.commit()

def getGListsOfUser(userid):
	cursor.execute('SELECT * FROM GList WHERE userid=?', (userid, ))
	return cursor.fetchall()

def getItemsOfGList(glistid):
	cursor.execute('SELECT * FROM Item WHERE glistid=?', (glistid, ))
	return cursor.fetchall()

def getItemsOfUser(userid):
	cursor.execute('SELECT * FROM Item INNER JOIN GList ON GList.id = Item.glistid WHERE userid=?', (userid, ))
	return cursor.fetchall()

def getUserId(name):
	cursor.execute('SELECT id FROM User WHERE name=?', (name, ))
	return int(cursor.fetchone()[0])

def getGListId(name):
	cursor.execute('SELECT id FROM GList WHERE name=?', (name, ))
	return int(cursor.fetchone()[0])

def getItemId(name):
	cursor.execute('SELECT id FROM Item WHERE name=?', (name, ))
	return int(cursor.fetchone()[0])



