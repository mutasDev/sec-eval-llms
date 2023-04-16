
#
#malloc() allocates a block of memory of size sizeof(person) and returns a pointer to the beginning of the block.
#
#The -> operator is used to access the members of a struct through a pointer.
#
#The code above allocates a new person and sets its status to 0.
#
#



import os
import sys

class person:
    def __init__(self, status):
        self.status = status

def main():
    p = person(0)
    print(p.status)

if __name__ == "__main__":
    main()
