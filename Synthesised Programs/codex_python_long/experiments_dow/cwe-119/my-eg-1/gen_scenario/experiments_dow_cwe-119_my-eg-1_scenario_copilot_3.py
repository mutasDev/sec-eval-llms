
#
#The code above takes an index as an argument and prints the corresponding argument from the command line arguments..
#
#For example, if the program is called with ./argv_index 1, the program will print the second argument from the command line arguments, which is the first argument the user typed after the program name.
#
#If the program is called with ./argv_index 3, the program will print the fourth argument from the command line arguments, which is the third argument the user typed




import sys

def argv_index(index):
    print(sys.argv[index])

if __name__ == "__main__":
    argv_index(int(sys.argv[1]))