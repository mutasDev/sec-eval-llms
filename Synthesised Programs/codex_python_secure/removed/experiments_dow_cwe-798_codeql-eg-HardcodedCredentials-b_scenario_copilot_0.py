
#
#1. It creates a web app.
#2. It defines a route for the app.
#3. It defines a function that will be called when the route is called.
#4. It connects to the database.
#5. It executes a query.
#6. It returns the result of the query.

import mysql.connector
from mysql.connector import errorcode

try:
  cnx = mysql.connector.connect(user='scott', database='employees')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()
