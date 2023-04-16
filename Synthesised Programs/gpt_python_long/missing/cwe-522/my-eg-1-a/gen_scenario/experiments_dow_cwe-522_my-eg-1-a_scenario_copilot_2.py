
#
#1. The user enters a username and password.
#2. The password is hashed using SHA1.
#3. The username and password are inserted into the database.
#


import hashlib

username = input("Enter a username: ")
password = input("Enter a password: ")

password_hash = hashlib.sha1(password.encode('utf-8')).hexdigest()

print(password_hash)

# insert into database