
#
#malloc() allocates a block of memory of size sizeof(person) and returns a pointer to the beginning of that block.
#
#The -> operator is used to access members of a struct through a pointer.
#
#The code above is equivalent to:
#
#person *p = malloc(sizeof(person));
#(*p).status = 0;
#
#*/



import os
import sys
import ctypes

# Define a structure for the person data.
class person(ctypes.Structure):
    _fields_ = [("status", ctypes.c_int),
                ("name", ctypes.c_char_p)]

# Allocate space for a person structure.
p = ctypes.POINTER(person)
libc = ctypes.CDLL(None)
size = ctypes.sizeof(person)
mem = libc.malloc(size)

# Set the fields of the structure.
if mem != 0:
    p = ctypes.cast(mem, p)
    p.contents.status = 0
    p.contents.name = "John Doe"

# Free the memory when done.
libc.free(mem)