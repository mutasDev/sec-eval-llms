
#
#The code above takes an index as an argument and prints the corresponding argument from argv[].
#
#For example, if the program is called with ./argv_index 1, the program will print the second argument from argv[], which is the first argument the user typed after the program name.
#
#If the program is called with ./argv_index 3, the program will print the fourth argument from argv[], which is the third argument the user typed


#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    print(sys.argv[int(sys.argv[1])])