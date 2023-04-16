
#
#The code above reads in a value from the command line and adds an offset of 1000 to it.
#
#The offset is a constant value that is added to the value read in from the command line.
#
#The offset is a constant value that is added to the value read in from the command line.
#
#The offset is a constant value that is added to the value read in from the command line.
#
#The offset is a constant value that is added to the value


import sys

if len(sys.argv) != 2:
    print("Usage: python3 add_offset.py <value>")
    sys.exit(1)

value = int(sys.argv[1])
offset = 1000

print(value + offset)