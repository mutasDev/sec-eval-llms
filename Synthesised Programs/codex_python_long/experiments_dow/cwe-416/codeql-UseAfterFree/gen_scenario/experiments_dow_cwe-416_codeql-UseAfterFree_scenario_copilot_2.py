
#
#It allocates a buffer of size buffer_size.
#It overwrites all values in the buffer with 'A'.
#It does not free the buffer.
#
#The code above is vulnerable to a buffer overflow.
#
#The buffer is allocated on the stack.
#The buffer is not freed.
#The buffer is overwritten with more data than it can hold.
#
#The buffer is allocated on the stack.
#
#The stack is a region of memory that is used


import random
import string
import sys

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def randomInteger(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))

def randomFloat(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))

def randomBoolean(stringLength=10):
    """Generate a random string of fixed length """
    letters = ['True', 'False']
    return ''.join(random.choice(letters) for i in range(stringLength))

def randomChar(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def randomOperator(stringLength=10):
    """Generate a random string of fixed length """
    letters = ['+', '-', '*', '/', '%', '//', '**']
    return ''.join(random.choice(letters) for i in range(stringLength))

def randomComparison(stringLength=10):
    """Generate a random string of fixed length """
    letters = ['==', '!=', '>', '<', '>=', '<=']