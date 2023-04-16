
#
#The code above is a simple registration form that takes the username and password from the user and hashes the password using the SHA256 algorithm.
#

import hashlib

password = input("Enter password: ")

# Hash a password for the first time, with a randomly-generated salt
salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                              salt, 100000)
pwdhash = binascii.hexlify(pwdhash)

# Check a password against an existing hash
old_salt = b'\xfa\x8c\x13\x8b\x15\x8e\x1a\xbf\x82\x16\x19\x1c\x1a\x06\x18\x8a\x05\x11\x1a\x11\x10\x16\x1a\x1c\x11\x1a\x1b\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a'