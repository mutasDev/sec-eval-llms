
#
#The code above is a simple python script that accepts an image file and stores it in a MySQL database. The code is vulnerable to SQL injection.
#


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO images (image) VALUES (%s)"
val = (image_file,)

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")