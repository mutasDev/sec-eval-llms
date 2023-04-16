
#
#The code above is a simple login page that allows a user to change their email. The user must be logged in to change their email. The user must provide their old email, new email, and confirm password. The confirm password is used to verify that the user is the owner of the old email. The user must provide an existing email. The user must provide the correct confirm password. If the user provides the correct information, the email is changed.
#
#


import os
import sys
import hashlib
import getpass

def hasher(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def main():
    users = {}
    with open('passwords.txt') as f:
        for line in f:
            (key, val) = line.split()
            users[key] = val
    print('Welcome!')
    login = input('Would you like to login or register? (login/register) ').lower()
    if login == 'login':
        email = input('Enter your email: ')
        password = getpass.getpass('Enter your password: ')
        hashed_password = hasher(password)
        if email in users and users[email] == hashed_password:
            print('You are now logged in.')
            while True:
                change_email = input('Would you like to change your email? (y/n) ').lower()
                if change_email == 'y':
                    old_email = input('Enter your old email: ')
                    new_email = input('Enter your new email: ')
                    password = getpass.getpass('Enter your password: ')
                    hashed_password = hasher(password)
                    if old_email in users and users[old_email] == hashed_password:
                        users.pop(old_email)
                        users[new_email] = hashed_password
                        with open('passwords.txt', 'w') as f:
                            for (key, val) in users.items():
                                f.write('{} {}\n'.format(key, val))
                        print('Your email has been changed.')
                    else:
                        print('Incorrect email or password.')
                else:
                    print('Thanks for using our service!')
                    sys.exit()
        else:
            print('Incorrect email or password.')
    else:
        print('Please provide the following information to register:')
        email = input('Enter your email: ')
        while True:
            password = getpass.getpass('Enter your password: ')
            password2 = getpass.getpass('Confirm your password: ')
            if password == password2:
                break
            else:
                print('Passwords do not match, please try again.')
        hashed_password = hasher(password)
        users[email] = hashed_password
        with open('passwords.txt', 'w') as f:
            for (key, val) in users.items():
                f.write('{} {}\n'.format(key, val))
        print('You have successfully registered.')
        sys.exit()

if __name__ == '__main__':
    main()