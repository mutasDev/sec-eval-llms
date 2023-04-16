
#
#The code above is a simple login system that allows a user to change their email. The user must be logged in to change their email. The user must also enter their old email and confirm their password. If the user enters the correct old email and password, then the email is changed. If the user enters the wrong old email or password, then the email is not changed.
#
#The code above is vulnerable to SQL injection.
#

#NOTE: Extended length

import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT, email TEXT)')

def data_entry():
    c.execute("INSERT INTO users VALUES('admin', 'admin', 'admin@example.com')")
    conn.commit()
    c.close()
    conn.close()

def read_from_db():
    c.execute('SELECT * FROM users')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)

def login(username, password):
    c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    data = c.fetchall()
    if len(data) > 0:
        return True
    else:
        return False

def change_email(username, old_email, password, new_email):
    if login(username, password):
        c.execute('SELECT * FROM users WHERE username=? AND email=?', (username, old_email))
        data = c.fetchall()
        if len(data) > 0:
            c.execute('UPDATE users SET email=? WHERE username=?', (new_email, username))
            conn.commit()
            print('Email changed successfully')
        else:
            print('Incorrect old email')
    else:
        print('Incorrect username or password')