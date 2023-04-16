
#
#The code above is a simple login page that takes the username and password from the user and checks if the username and password are correct. If they are correct, the user is redirected to the session page. If they are incorrect, the user is told that the username or password is incorrect.
#


import hashlib

def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    
def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

# Store password hashes in database
new_pass = hash_password('mypassword')
print(new_pass)
# Check a password against a stored password
old_pass = '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8:6dd27ecf2340'
print(check_password(old_pass, 'mypassword'))