
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

def read_file(filename):
    if not os.path.isabs(filename):
        raise ValueError("Filename must be an absolute path.")
    if not os.path.exists(filename):
        raise ValueError("File does not exist.")
    if not os.path.isfile(filename):
        raise ValueError("Filename must be a regular file.")

    with open(filename, 'r') as f:
        return f.read()