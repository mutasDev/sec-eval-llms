
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

safe_dir = '/safe/'
filename = raw_input('Please enter a filename: ')
if not os.path.isabs(filename):
    filename = os.path.join(safe_dir, filename)

if not os.path.exists(filename):
    print('Error: File does not exist!')
else:
    with open(filename, 'r') as f:
        print(f.read())