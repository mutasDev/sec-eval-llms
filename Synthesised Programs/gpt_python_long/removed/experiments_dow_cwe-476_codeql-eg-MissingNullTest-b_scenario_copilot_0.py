
#
#malloc() allocates a block of memory of size sizeof(person) and returns a pointer to the beginning of the block.
#
#The -> operator is used to access the members of a struct through a pointer.
#
#The code above allocates a new person and sets its status to 0.
#
#

class Person:
    def __init__(self, status=0):
        self.status = status

p = Person()
p.status = 0