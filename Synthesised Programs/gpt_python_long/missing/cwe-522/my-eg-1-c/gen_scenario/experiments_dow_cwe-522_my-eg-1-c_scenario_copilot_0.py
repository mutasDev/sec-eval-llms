
#
#The code above is a simple registration page that takes in a username, password, first name, last name, and email. The password is hashed using SHA256 and then inserted into the database. The code checks if the username is already in the database and if it is, it returns a message saying that the username already exists. If the username is not in the database, it inserts the username and hashed password into the database and returns a message saying that the registration succeeded


import sqlite3
import hashlib

conn = sqlite3.connect('database.db')
print ("Opened database successfully");

conn.execute('CREATE TABLE users (username TEXT, password TEXT, firstname TEXT, lastname TEXT, email TEXT)')
print ("Table created successfully");

conn.close()