
#empty


import sys

def add_1000(val):
    """Adds 1000 to the given value."""
    return val + 1000

def main():
    """Reads a value from the command line and adds 1000 to it."""
    if len(sys.argv) != 2:
        print("Usage: {} <value>".format(sys.argv[0]))
        return 1

    val = int(sys.argv[1])
    print(add_1000(val))
    return 0

if __name__ == "__main__":
    sys.exit(main())