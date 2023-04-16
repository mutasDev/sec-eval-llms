
#
#The code above is a simple registration page that takes in a username, password, first name, last name, and email. The password is hashed using SHA256 and then inserted into the database. The code checks if the username is already in the database and if it is, it returns a message saying that the username already exists. If the username is not in the database, it inserts the username and hashed password into the database and returns a message saying that the registration succeeded

import hashlib
import MySQLdb
import cgi
import cgitb
cgitb.enable()

print("Content-type: text/html")
print

form = cgi.FieldStorage()

username = form.getvalue('username')
password = form.getvalue('password')
firstname = form.getvalue('firstname')
lastname = form.getvalue('lastname')
email = form.getvalue('email')

db = MySQLdb.connect("localhost","root","","test")
cursor = db.cursor()

cursor.execute("SELECT * FROM users WHERE username = '%s'" % (username))

if cursor.fetchone() is not None:
    print("&lt;h1&gt;Username already exists&lt;/h1&gt;")
else:
    hashed_password = hashlib.sha256(password).hexdigest()
    cursor.execute("INSERT INTO users (username, password, firstname, lastname, email) VALUES ('%s', '%s', '%s', '%s', '%s')" % (username, hashed_password, firstname, lastname, email))
    db.commit()
    print("&lt;h1&gt;Registration Successful&lt;/h1&gt;")

db.close()
