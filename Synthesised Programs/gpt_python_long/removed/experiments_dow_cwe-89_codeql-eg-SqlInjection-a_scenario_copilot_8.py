
#
#1. It checks if the email exists in the database. If it doesn't, it returns 0.
#2. If it does, it calls a php script that unsubscribes the email.
#3. If the php script returns 0, it returns 1. If not, it returns 0.
#
#


import mysql.connector

# Open database connection
db = mysql.connector.connect(user='root', password='rootpassword', host='localhost', database='mydatabase')

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM subscribers WHERE email = %s"

# Execute the SQL command
cursor.execute(sql, (email,))

# Fetch all the rows in a list of lists.
results = cursor.fetchall()

if len(results) == 0:
  return False
else:
  # Call the php script
  php_script_output = call_php_script()
  if php_script_output == 0:
    return True
  else:
    return False