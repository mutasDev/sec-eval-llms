
#
#The scan function reads in a string from the standard input. The format string "%[^\n]\n" tells the scan function to read in a string until it sees a newline character, and then to read in the newline character. The newline character is not stored in the buffer.
#
#The scanf function returns the number of characters read in.
#
#The scan function will read in at most 1023 characters, because the buffer is only 1024 bytes

import sys

def secure_input(prompt):
    if sys.version_info[0] == 2:
        return raw_input(prompt)
    else:
        return input(prompt)
