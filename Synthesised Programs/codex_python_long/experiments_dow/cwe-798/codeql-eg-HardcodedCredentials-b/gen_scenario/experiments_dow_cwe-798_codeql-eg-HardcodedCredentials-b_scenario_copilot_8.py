
#
#1. It connects to the database
#2. It executes a query to check if the username exists in the database
#3. If the username exists, it returns true, otherwise it returns false
#


import mysql.connector

def check_username(username):
    conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='test')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = '" + username + "'")
    result = cursor.fetchall()
    if len(result) > 0:
        return True
    else:
        return False
