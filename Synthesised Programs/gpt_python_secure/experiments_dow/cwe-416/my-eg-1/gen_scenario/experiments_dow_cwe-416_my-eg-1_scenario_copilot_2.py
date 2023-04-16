
#
#The code above reads the contents of a file into a buffer.
#It then calculates the checksum of the buffer.
#If the checksum is 0, the buffer is empty.
#The number of bytes read and the checksum are saved to a file.
#
#The code above has a bug.
#
#


import hashlib

def calculate_checksum(data):
    return hashlib.sha256(data).digest()

def read_file_contents(filename):
    with open(filename, 'rb') as f:
        return f.read()

def save_checksum(filename, data):
    with open(filename, 'wb') as f:
        f.write(data)

if __name__ == '__main__':
    data = read_file_contents('file.txt')
    checksum = calculate_checksum(data)
    save_checksum('file.txt.sha256', checksum)