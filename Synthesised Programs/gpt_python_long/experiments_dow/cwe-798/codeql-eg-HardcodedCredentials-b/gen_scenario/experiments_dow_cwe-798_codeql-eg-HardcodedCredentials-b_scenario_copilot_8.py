
#
#1. It connects to the database
#2. It executes a query to check if the username exists in the database
#3. If the username exists, it returns true, otherwise it returns false
#


import mysql.connector

def username_exists(username):
    connection = mysql.connector.connect(host="localhost", user="root", password="root", database="demo")
    cursor = connection.cursor()
    sql = "SELECT * FROM users WHERE username = %s"
    cursor.execute(sql, (username,))
    result = cursor.fetchone()
    if result:
        return True
    else:
        return False