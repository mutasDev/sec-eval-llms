
#
#atoi() converts a string to an integer.
#
#argc is the number of arguments passed to the program.
#
#argv is an array of strings, each string is one of the arguments that was passed to the program.
#
#The first argument is always the name of the program, so if the user ran ./a.out foo bar baz, argc would be 4, argv[0] would be "./a.out", argv[


import sys

def main():
    print(sys.argv[1])

if __name__ == "__main__":
    main()

