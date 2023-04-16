
#
#malloc() allocates a block of memory of size sizeof(person) and returns a pointer to the beginning of the block.
#
#The -> operator is used to access the members of a struct when the struct is pointed to by a pointer.
#
#The code above allocates a new person and sets the status to 0.
#
#

class person:
    def __init__(self, status = 0):
        self.status = status

p = person()
p.status = 0