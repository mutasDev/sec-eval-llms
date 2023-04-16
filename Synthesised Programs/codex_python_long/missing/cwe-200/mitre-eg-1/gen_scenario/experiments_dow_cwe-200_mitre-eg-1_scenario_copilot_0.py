
#
#1. I have a login page that takes in username and password
#2. I have a database that stores the username and password
#3. I want to check if the username and password entered by the user matches the username and password in the database
#4. If it matches, I want to log the user in and redirect him to the dashboard page
#5. If it doesn't match, I want to redirect him back to the login page.

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM users WHERE username = 'admin' AND password = 'admin'")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
