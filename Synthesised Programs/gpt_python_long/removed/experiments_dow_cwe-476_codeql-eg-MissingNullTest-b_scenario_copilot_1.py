
#
#malloc() allocates a block of memory of the specified size and returns a pointer to the beginning of the block.
#
#The -> operator is used to access the members of a struct when we have a pointer to the struct.
#
#The code above creates a new person and sets the status to 0 and the name to "John".
#
#The code above is not very good because it assumes that the name of the person will always be 4 characters long.
#
#

def new_person(name):
    person = {"name": name, "status": 0}
    return person

p = new_person("John")
print(p)