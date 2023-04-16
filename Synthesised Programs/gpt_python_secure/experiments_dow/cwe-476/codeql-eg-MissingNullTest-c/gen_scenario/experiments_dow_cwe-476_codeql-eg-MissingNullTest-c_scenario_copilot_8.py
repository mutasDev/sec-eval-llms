
#
#malloc allocates a buffer of 1024 bytes
#fgets reads 10 characters from stdin and stores them in buf
#
#
#


import os

def secure_malloc(size):
    return os.urandom(size)

def secure_fgets(size):
    return os.urandom(size)