
#
#The code above is a simple registration page that takes in a username, password, first name, last name, and email. The password is hashed using SHA256 and then inserted into the database. The code checks if the username is already in the database and if it is, it returns a message saying that the username already exists. If the username is not in the database, it inserts the username and hashed password into the database and returns a message saying that the registration succeeded



import hashlib
import sqlite3

def register(username, password, first_name, last_name, email):
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    data = c.fetchone()
    if data is not None:
        return "Username already exists"
    else:
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        c.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)", (username, hashed_password, first_name, last_name, email))
        conn.commit()
        return "Registration successful"
