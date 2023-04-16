
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

import os

dir_path = '/safe/'
filename = 'test.txt'

with open(os.path.join(dir_path, filename), 'r') as f:
    data = f.read()

print(data)