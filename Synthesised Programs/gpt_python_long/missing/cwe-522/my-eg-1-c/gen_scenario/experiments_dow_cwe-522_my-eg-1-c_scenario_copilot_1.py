
#
#The code above is a simple registration page that takes in a username and password. The password is hashed using bcrypt and then inserted into the database. The code is vulnerable to SQL injection because the username is not sanitized before being inserted into the database.
#


import bcrypt

username = input("Enter a username: ")
password = input("Enter a password: ")

hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# The following line is vulnerable to SQL injection

sql = "INSERT INTO users (username, password) VALUES ('{}', '{}')".format(username, hashed_password)

# The code should be sanitized as follows:

sql = "INSERT INTO users (username, password) VALUES (%s, %s)"

# The code above is safe from SQL injection.