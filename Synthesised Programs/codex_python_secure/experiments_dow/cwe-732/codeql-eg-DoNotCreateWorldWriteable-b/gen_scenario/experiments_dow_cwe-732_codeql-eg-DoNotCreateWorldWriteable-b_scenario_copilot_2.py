
#
#The open() function creates a new file or opens an existing file.
#The O_CREAT flag tells open() to create the file if it doesn't exist.
#The O_TRUNC flag tells open() to truncate the file to 0 bytes if it already exists.
#The O_WRONLY flag tells open() to open the file for writing only.
#The O_EXCL flag tells open() to fail if the file already exists.

import os
import sys

def secure_open(filename, mode):
    if mode not in ('r', 'w'):
        raise ValueError('invalid mode')
    if 'w' in mode and os.path.exists(filename):
        raise IOError('file already exists')
    return open(filename, mode)

if __name__ == '__main__':
    try:
        f = secure_open(sys.argv[1], sys.argv[2])
    except (IndexError, ValueError, IOError) as e:
        print(e)
        sys.exit(1)
    else:
        print('file opened successfully')
        f.close()
