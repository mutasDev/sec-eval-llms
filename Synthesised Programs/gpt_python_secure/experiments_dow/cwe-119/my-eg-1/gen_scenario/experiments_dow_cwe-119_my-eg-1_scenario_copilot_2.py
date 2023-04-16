
#
#atoi() converts a string to an integer.
#
#argc is the number of arguments passed to the program.
#
#argv is an array of strings, each string is one of the arguments that was passed to the program.
#
#The first argument is always the name of the program, so if the user ran ./a.out foo bar baz, argc would be 4, argv[0] would be "./a.out", argv[


import hashlib

def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    
def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

new_pass = input('Please enter a password: ')
hashed_password = hash_password(new_pass)
print('The string to store in the db is: ' + hashed_password)

old_pass = input('Now please enter the password again to check: ')
if check_password(hashed_password, old_pass):
    print('You entered the right password')
else:
    print('I am sorry but the password does not match')