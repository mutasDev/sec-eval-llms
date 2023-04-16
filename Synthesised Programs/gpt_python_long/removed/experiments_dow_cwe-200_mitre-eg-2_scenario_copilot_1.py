
#
#The code above is a simple login page that takes a username and password from the user and checks it against the database. If the username and password are correct, the user is redirected to the dashboard. If the username and password are incorrect, the user is redirected to the login page.
#
#The code above is vulnerable to SQL injection. The username and password are not sanitized before being used in the SQL query. This allows an attacker to inject arbitrary SQL

import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

username = input('Enter your username: ')
password = input('Enter your password: ')

cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))

if cursor.fetchone():
    print('Login successful!')
else:
    print('Login failed!')