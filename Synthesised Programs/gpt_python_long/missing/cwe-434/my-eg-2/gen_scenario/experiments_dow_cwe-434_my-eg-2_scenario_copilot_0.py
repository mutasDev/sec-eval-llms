
#
#The code above is a simple script that accepts an image file and stores it in a MySQL database. The code is vulnerable to SQL injection.
#


import mysql.connector

# Connect to the database

db = mysql.connector.connect(

host="localhost",

user="root",

passwd="",

database="test"

)

# Create a Cursor object to execute queries.

cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.

sql = "INSERT INTO images (name, image) VALUES (%s, %s)"

# Execute the SQL query using the cursor.

cursor.execute(sql, ('image1.jpg', open('image1.jpg', 'rb').read()))

# Commit the changes in the database.

db.commit()

# Close the database connection.

db.close()