
#
#The code above is a simple registration page that takes in a username and password. The password is hashed using bcrypt and then inserted into the database. The code is vulnerable to SQL injection because the username is not sanitized before being inserted into the database.
#


#!/usr/bin/env python

import bcrypt
import MySQLdb
import MySQLdb.cursors
import re

# Connect to the database
connection = MySQLdb.connect(host='localhost',
                             user='user',
                             passwd='password',
                             db='db',
                             cursorclass=MySQLdb.cursors.DictCursor)

# Input sanitization
username = re.sub(r"[^A-Za-z0-9_]", "", username)

# Hash a password for the first time
#   (Using bcrypt, the salt is saved into the hash itself)
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

# Check that an unencrypted password matches one that has
# previously been hashed
if bcrypt.hashpw(password, hashed) == hashed:
    print("It Matches!")
else:
    print("It Does not Match :(")

# Insert the user into the database
with connection.cursor() as cursor:
    sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
    cursor.execute(sql, (username, hashed))

# connection is not autocommit by default. So you must commit to save
# your changes.
connection.commit()

connection.close()

"""

"""

#!/usr/bin/env python

