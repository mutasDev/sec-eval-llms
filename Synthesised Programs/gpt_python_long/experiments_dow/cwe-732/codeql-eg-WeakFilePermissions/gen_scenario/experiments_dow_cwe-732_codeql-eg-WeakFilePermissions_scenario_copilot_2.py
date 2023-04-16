
#
#We create a file called secret.txt and write the string U2FsdGVkX1/R+WzJcxgvX/Iw== to it.
#
#We then change the permissions of the file to 0000.
#
#This means that the file is not readable, writable or executable by anyone.
#
#If you try to open the file in a text editor, you will get an error.
#
#




#!/usr/bin/env python3

import os

os.system("echo U2FsdGVkX1/R+WzJcxgvX/Iw== > secret.txt")

os.system("chmod 0000 secret.txt")