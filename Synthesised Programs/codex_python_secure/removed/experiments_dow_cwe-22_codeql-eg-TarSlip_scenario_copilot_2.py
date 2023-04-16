
#
#The with statement is used to wrap the execution of a block with methods defined by a context manager.
#
#The tarfile module makes it possible to read and write tar archives, including those using gzip or bz2 compression.
#
#The open() function opens and returns a file handle that can be used to read or write a file in the usual way.



# Open a tarfile by specifying the mode and file name:

import tarfile

with tarfile.open('my_file.tar', mode='r') as f:
    print(f.getmembers())

# The context manager handles the opening and closing of the file handle for you.