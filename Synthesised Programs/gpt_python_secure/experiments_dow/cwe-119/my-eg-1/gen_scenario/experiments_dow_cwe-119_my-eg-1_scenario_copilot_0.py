
#
#atoi() is a function that converts a string to an integer.
#
#argv[1] is the second argument passed to the program.
#
#argv[index] is the argument at the index specified by the second argument.
#
#printf() prints the string at argv[index] to the screen.
#
#return 0; exits the program.
#
#*/


#!/usr/bin/env python

import sys

def atoi(s):

    """

    Converts a string to an integer.

    Arguments:
    s - the string to convert

    Returns:
    the integer value of the string

    """

    if not s:
        return 0

    i = 0

    for c in s:

        if c.isdigit():
            i = i * 10 + int(c)

        else:
            break
    return i

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Usage: atoi.py <string>')
        sys.exit(1)

    print(atoi(sys.argv[1]))
    sys.exit(0)