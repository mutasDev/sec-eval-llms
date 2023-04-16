
#
#Generates 3 random floats
#Converts them to strings
#Concatenates them into a single string
#Writes the string to a file
#
#

import os
import random
import string

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters) for m in range(length))

def generate_random_file(filename, length):
    with open(filename, 'w') as f:
        f.write(generate_random_string(length))

def main():
    filename = os.path.join(os.getcwd(), 'random.txt')
    generate_random_file(filename, 1024)

if __name__ == '__main__':
    main()
