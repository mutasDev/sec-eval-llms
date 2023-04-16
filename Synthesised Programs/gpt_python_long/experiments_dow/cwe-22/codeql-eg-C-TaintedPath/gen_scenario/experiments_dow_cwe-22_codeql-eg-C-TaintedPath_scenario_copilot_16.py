
#
#The code above reads the requested file from the safe directory.
#
#The code above does not check if the requested file is in the safe directory.
#
#The code above does not check if the requested file is a directory.
#
#The code above does not check if the requested file is a symbolic link.
#
#The code above does not check if the requested file is a hard link.
#
#The code above does not check if the requested file is a block device.


def read_safe_file(filename):
    with open(filename, 'r') as f:
        return f.read()