
#
#malloc() allocates a block of memory of size sizeof(person) and returns a pointer to the beginning of the block.
#
#The cast (person *) is not necessary, but it is good practice to include it.
#
#The -> operator is used to access the fields of a struct through a pointer.
#
#The code above allocates a new person and sets the status field to 0.
#
#


import os

class person:

    def __init__(self):

        self.status = 0

        self.name = ""

        self.age = 0

    def set_status(self, status):

        self.status = status

    def set_name(self, name):

        self.name = name

    def set_age(self, age):

        self.age = age

    def get_status(self):

        return self.status

    def get_name(self):

        return self.name

    def get_age(self):

        return self.age

def main():

    p = person()

    p.set_status(0)

    p.set_name(os.urandom(16))

    p.set_age(0)

    print(p.get_status())

    print(p.get_name())

    print(p.get_age())

if __name__ == "__main__":
    main()
