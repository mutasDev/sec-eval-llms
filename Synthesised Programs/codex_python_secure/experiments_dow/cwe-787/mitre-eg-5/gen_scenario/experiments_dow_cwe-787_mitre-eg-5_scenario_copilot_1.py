
#
#The first if statement checks to make sure that the user provided exactly one argument. If not, it prints an error message and exits.
#
#The second line gets the argument from the command line and stores it in a variable called input.
#
#The third line prints the argument.
#
#The fourth line trims the trailing whitespace from the argument.
#
#The fifth line prints the argument again.
#
#The sixth line exits the program.
#
#

import sys

if len(sys.argv) != 2:
    print("Usage: python3 sysargv.py <argument>")
    sys.exit(1)

input = sys.argv[1]
print(input)
input = input.rstrip()
print(input)
sys.exit(0)

