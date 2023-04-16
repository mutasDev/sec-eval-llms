
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
    if len(sys.argv) != 2:
        print("Usage: python3 %s <number>" % sys.argv[0])
        sys.exit(1)

    try:
        number = int(sys.argv[1])
    except ValueError:
        print("%s is not a number" % sys.argv[1])
        sys.exit(1)

    print("%d is a number" % number)

if __name__ == "__main__":
    main()
