
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

def secure_atoi(s):
    value = 0
    try:
        value = int(s)
    except ValueError:
        print("Not a valid integer!")
        raise SystemExit(1)
        
    return value
