
#
#The code above is a simple login system that allows a user to change their email. The user must be logged in to change their email. The user must also enter their old email and confirm their password. If the user enters the correct old email and password, then the email is changed. If the user enters the wrong old email or password, then the email is not changed.
#
#The code above is vulnerable to SQL injection.
#


import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

username = input('Enter your username: ')
password = input('Enter your password: ')

c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))

user = c.fetchone()

if user:
    old_email = input('Enter your old email: ')
    new_email = input('Enter your new email: ')

    c.execute('UPDATE users SET email = ? WHERE email = ?', (new_email, old_email))
    conn.commit()
    print('Email updated')
else:
    print('Invalid login')