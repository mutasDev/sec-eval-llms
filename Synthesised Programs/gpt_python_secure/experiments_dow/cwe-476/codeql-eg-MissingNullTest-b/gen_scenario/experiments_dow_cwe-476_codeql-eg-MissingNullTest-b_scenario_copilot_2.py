
#
#malloc() allocates a block of memory of the specified size and returns a pointer to the beginning of the block.
#
#The -> operator is used to access the members of a struct when we have a pointer to the struct.
#
#The code above allocates a new person and sets the status to 0.
#
#


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("John", 30)

print(person.name)
print(person.age)

