
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


import sys

def main():
    print(sys.argv[int(sys.argv[1])])

if __name__ == "__main__":
    main()

