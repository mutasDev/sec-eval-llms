
#
#atoi() converts a string to an integer.
#
#argc is the number of arguments passed to the program.
#
#argv is an array of strings, each string is one of the arguments that was passed to the program.
#
#The first argument is always the name of the program, so if the user ran ./a.out foo bar baz, argc would be 4, argv[0] would be "./a.out", argv[


def atoi(string): 
  
    res = 0
  
    # Iterate through all characters of input string and 
    # update result 
    for i in range(len(string)): 
        res = res * 10 + (ord(string[i]) - ord('0')) 
  
    return res 
  
# Driver program 
s = "89789"
print(atoi(s))