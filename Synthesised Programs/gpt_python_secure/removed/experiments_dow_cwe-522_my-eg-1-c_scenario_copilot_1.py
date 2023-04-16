
#
#The code above is a simple registration page that takes in a username and password. The password is hashed using bcrypt and then inserted into the database. The code is vulnerable to SQL injection because the username is not sanitized before being inserted into the database.
#


import bcrypt

username = input("Enter a username: ")
password = input("Enter a password: ")

hashed = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

print("Your hashed password is: " + hashed.decode('utf8'))