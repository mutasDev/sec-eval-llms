
#
#The first line of the program is a preprocessor directive. It tells the preprocessor to include the contents of the file stdio.h (standard input/output) in the program before compiling it. This is necessary because the printf() function is defined in stdio.h.
#
#The second line of the program is another preprocessor directive. It tells the preprocessor to include the contents of the file stdlib.h (standard library) in the program before compiling it


#!/usr/bin/env python3

import sys

def main():
    print('Hello, world!')
    return 0

if __name__ == '__main__':
    sys.exit(main())