
#
#1. The user enters a username and password.
#2. The password is hashed using SHA1.
#3. The username and password are inserted into the database.
#



import hashlib
import sqlite3

def create_user(username, password):
    password_hash = hashlib.sha1(password).hexdigest()
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?, ?)", (username, password_hash))
    conn.commit()
    conn.close()

create_user('admin', 'password')
