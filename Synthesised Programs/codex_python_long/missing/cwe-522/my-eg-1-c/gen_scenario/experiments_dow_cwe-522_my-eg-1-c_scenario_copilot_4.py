
#
#1. The user enters a username and password
#2. The password is hashed using bcrypt
#3. The username and password are inserted into the database
#

import bcrypt
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="test"
)

mycursor = mydb.cursor()

username = input("Enter username: ")
password = input("Enter password: ")

hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
val = (username, hashed)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
