
#
#The scan function reads in a string from the standard input. The format string "%[^\n]\n" tells the scan function to read in a string until it sees a newline character, and then to read in the newline character. The newline character is not stored in the buffer.
#
#The scan function returns the number of characters read in.
#
#The scan function will read in at most 1023 characters, because the buffer is only 1024 bytes

def get_input():
    return input('Please type in the string:')

buffer = 1024

def scan(string):
    string_size = len(string)

    if string_size > buffer:
        return buffer
    else:
        return string_size
