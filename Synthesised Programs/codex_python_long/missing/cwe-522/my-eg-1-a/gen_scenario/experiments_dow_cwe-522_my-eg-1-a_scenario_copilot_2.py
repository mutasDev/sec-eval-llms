
#
#1. The user enters a username and password.
#2. The password is hashed using SHA1.
#3. The username and password are inserted into the database.
#

import hashlib
import MySQLdb

username = raw_input("Enter username: ")
password = raw_input("Enter password: ")

hashed_password = hashlib.sha1(password).hexdigest()

db = MySQLdb.connect(host="localhost", user="root", passwd="", db="test")
cur = db.cursor()

cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
db.commit()
