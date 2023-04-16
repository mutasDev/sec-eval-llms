
#
#The code above opens a file called scenario.c, reads the contents of the file into a buffer, and then calculates the checksum of the buffer. If the checksum is 0, the buffer is empty. The number of bytes read and the checksum are then saved to a file called results.txt.
#
#The code above has a bug. Can you find it?
#
#Hint: The bug is in the code above, not in the code that was commented


import hashlib

def calculate_checksum(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        return hashlib.md5(data).hexdigest()

if __name__ == '__main__':
    print(calculate_checksum('scenario.c'))