
#
# atoi is a function that converts a string to an integer.
#
# argv[1] is the second argument passed to the program.
#
# argv[index] is the argument at the index specified by the second argument.
#
# print prints the string at argv[index] to the screen.
#
# return 0; exits the program.
#
import sys
def atoi(str):
    index = 1
    if len(sys.argv) < 2:
        print("Error: Expected at least one argument.")
        exit(1)

    while index < len(sys.argv):
        print(atoi(sys.argv[index]))
        index = index + 1


main()
