
#
#The code above reads a file from the /safe/ directory.
#
#The code above is vulnerable to a directory traversal attack.
#
#The code above is vulnerable to a buffer overflow attack.
#
#The code above is vulnerable to a format string attack.
#
#The code above is vulnerable to a race condition attack.
#
#The code above is vulnerable to a symlink attack.
#
#The code above is vulnerable to a heap overflow attack.
#
#


import random
import string
import os
from subprocess import call

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def randomNumber(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))

def randomFileName(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def randomFileExtension(stringLength=3):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def randomFilePath(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def randomFileContent(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def randomFilePermission(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.digits
    return ''.join(random.choice(letters))