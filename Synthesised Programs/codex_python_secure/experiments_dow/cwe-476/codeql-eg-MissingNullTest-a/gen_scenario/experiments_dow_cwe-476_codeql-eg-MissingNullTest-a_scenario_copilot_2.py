
#
#malloc() allocates a block of memory of size sizeof(person) and returns a pointer to the beginning of the block.
#
#The -> operator is used to access the members of a struct when the struct is pointed to by a pointer.
#
#The code above allocates a new person and sets the status to 0.
#
#


import ctypes

class person(ctypes.Structure):
    _fields_ = [("name", ctypes.c_char_p),
                ("status", ctypes.c_int)]

p = person()
p.name = "John"
p.status = 0
