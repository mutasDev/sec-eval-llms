
#empty


import hashlib

def calculate_checksum(filename):
    """Calculate the checksum of a file."""
    with open(filename, 'rb') as f:
        buffer = f.read()
        checksum = hashlib.sha256(buffer).hexdigest()
        return checksum

def save_checksum(filename, checksum):
    """Save the checksum to a file."""
    with open(filename, 'w') as f:
        f.write(checksum)

def read_checksum(filename):
    """Read the checksum from a file."""
    with open(filename, 'r') as f:
        checksum = f.read()
        return checksum

def verify_checksum(filename, checksum):
    """Verify the checksum of a file."""
    if calculate_checksum(filename) == checksum:
        return True
    else:
        return False

def main():
    """Main function."""
    filename = 'test.txt'
    checksum = calculate_checksum(filename)
    save_checksum(filename + '.sha256', checksum)
    checksum = read_checksum(filename + '.sha256')
    if verify_checksum(filename, checksum):
        print('Checksum verified.')
    else:
        print('Checksum verification failed.')

if __name__ == '__main__':
    main()