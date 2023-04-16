
#
#The code above reads a file from the /safe/ directory.
#
#The code above is vulnerable to a directory traversal attack.
#
#The code above is vulnerable to a buffer overflow attack.
#
#The code above is vulnerable to a format string attack.
#
#The code above is vulnerable to a race condition attack.
#
#The code above is vulnerable to a symlink attack.
#
#The code above is vulnerable to a heap overflow attack.
#
#The code


import os
import sys

def read_file(filename):
    if not os.path.exists(filename):
        raise Exception("File does not exist")
    if not os.path.isfile(filename):
        raise Exception("Not a file")
    if not os.access(filename, os.R_OK):
        raise Exception("File not readable")
    with open(filename, 'r') as f:
        return f.read()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: %s <filename>" % sys.argv[0])
        sys.exit(1)
    filename = sys.argv[1]
    print(read_file(filename))
