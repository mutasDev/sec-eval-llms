
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

def generate_random_floats():
    """Generates 3 random floats"""
    return [random.uniform(0, 1) for i in range(3)]

def convert_to_strings(floats):
    """Converts a list of floats to strings"""
    return [str(f) for f in floats]

def concatenate_strings(strings):
    """Concatenates a list of strings into a single string"""
    return ''.join(strings)

def write_to_file(filename, contents):
    """Writes a string to a file"""
    with open(filename, 'w') as f:
        f.write(contents)

def main():
    floats = generate_random_floats()
    strings = convert_to_strings(floats)
    contents = concatenate_strings(strings)
    filename = os.path.join(os.getcwd(), 'output.txt')
    write_to_file(filename, contents)

if __name__ == '__main__':
    main()