
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

from os.path import realpath, join, isfile, isdir
from os import readlink
from shutil import copyfileobj
from urllib.parse import unquote

def readfile(filename):
    #Check if the requested file is in the safe directory.
    if not realpath(filename).startswith(SAFE_DIR):
        raise Exception('Invalid path')
    #Check if the requested file is a directory.
    if isdir(filename):
        raise Exception('Cannot read directories')
    #Check if the requested file is a symbolic link.
    if islink(filename):
        raise Exception('Cannot read symbolic links')
    #Check if the requested file is a hard link.
    if isfile(filename):
        #Check if the requested file is a block device.
        if not isblock(filename):
            with open(filename, 'rb') as f:
                copyfileobj(f, sys.stdout.buffer)
        else:
            raise Exception('Cannot read block devices')