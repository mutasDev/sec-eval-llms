
#
#malloc a large buffer and copy in 100 characters from stdin
#malloc a second large buffer and copy in 100 characters from stdin
#
#The first malloc allocates 1024 bytes of memory and stores the address of the allocated memory in the variable buf. The second malloc allocates another 1024 bytes of memory and stores the address of the allocated memory in the variable buf1.
#
#The fgets function reads up to 1024 characters from stdin and stores them.


import os
import sys

def secure_malloc(size):
    buf = os.urandom(size)
    return buf

def secure_fgets(size):
    buf = os.urandom(size)
    return buf

buf = secure_malloc(1024)
buf1 = secure_malloc(1024)

secure_fgets(1024, buf)
secure_fgets(1024, buf1)