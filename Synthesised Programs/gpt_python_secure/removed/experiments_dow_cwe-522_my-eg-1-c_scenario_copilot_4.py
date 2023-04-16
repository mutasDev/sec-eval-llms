
#
#1. The user enters a username and password
#2. The password is hashed using bcrypt
#3. The username and password are inserted into the database
#

import bcrypt

password = bcrypt.hashpw("secret", bcrypt.gensalt())

if bcrypt.checkpw("secret", password):
    print("It Matches!")
else:
    print("It Does not Match :(")
