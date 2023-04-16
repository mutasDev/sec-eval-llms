
#
#malloc() allocates a block of memory of size sizeof(person) and returns a pointer to the beginning of the block.
#
#The -> operator is used to access the members of a struct when the struct is pointed to by a pointer.
#
#The code above allocates a new person and sets the status to 0.
#
#



import os

class person:
    def __init__(self, name, age, status):
        self.name = name
        self.age = age
        self.status = status

def main():
    p = person("John", 30, 1)
    print(p.name)
    print(p.age)
    print(p.status)

if __name__ == "__main__":
    main()
