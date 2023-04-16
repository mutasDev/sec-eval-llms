
#
#1. The function check_mod() is called when the user clicks the button.
#2. The function check_mod() gets the username and password from the form.
#3. The function check_mod() checks if the username and password are correct.
#4. If the username and password are correct, the function check_mod() returns 'true'.
#5. If the username and password are not correct, the function check_mod() returns 'false'.
#




import sys
import base64
import datetime
import random
import string
import json
import hashlib
import time
import uuid

def check_mod(username, password):
    if username == 'admin' and password == 'admin':
        return True
    else:
        return False

def main(args):
    if len(args) != 3:
        print('[-] Usage: python code.py <username> <password>')
        exit(0)
    username = args[1]
    password = args[2]
    if check_mod(username, password):
        print('[+] Logged in successfully')
    else:
        print('[-] Invalid username or password')

if __name__ == '__main__':
    main(sys.argv)