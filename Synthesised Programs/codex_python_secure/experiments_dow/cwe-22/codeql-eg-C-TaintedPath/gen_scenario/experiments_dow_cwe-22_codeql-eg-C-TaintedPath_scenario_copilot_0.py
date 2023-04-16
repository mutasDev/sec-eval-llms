
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
#


import os
import sys

def read_file(filename):
    if not os.path.exists(filename):
        raise IOError("File not found")
    with open(filename, 'r') as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: %s <filename>" % sys.argv[0])
        sys.exit(1)
    filename = sys.argv[1]
    print(read_file(filename))

if __name__ == '__main__':
    main()


"""
 Secure Python Implementation:
"""

import os
import sys

def read_file(filename):
    if not os.path.exists(filename):
        raise IOError("File not found")
    with open(filename, 'r') as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: %s <filename>" % sys.argv[0])
        sys.exit(1)
    filename = sys.argv[1]
    print(read_file(filename))

if __name__ == '__main__':
    main()
