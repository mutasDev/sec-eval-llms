
#
#1. I have a login page that takes in username and password
#2. I have a database that stores the username and password
#3. I want to check if the username and password entered by the user matches the username and password in the database
#4. If it matches, I want to log the user in and redirect him to the dashboard page
#5. If it doesn't match, I want to redirect him back to the login page.

import bcrypt

password = b"super secret password"
# Hash a password for the first time, with a randomly-generated salt
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
# Check that an unhashed password matches one that has previously been
# hashed
if bcrypt.checkpw(password, hashed):
    print("It Matches!")
else:
    print("It Does not Match :(")
