
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

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 add_offset.py <number>")
        sys.exit(1)
    try:
        number = int(sys.argv[1])
    except ValueError:
        print("Usage: python3 add_offset.py <number>")
        sys.exit(1)
    print(number + 1000)

if __name__ == "__main__":
    main()
