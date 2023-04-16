
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

class Person:
    def __init__(self, status=0):
        self.status = status

p = Person()
print(p.status)