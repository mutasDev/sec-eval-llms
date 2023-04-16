
#
#The code above takes in a command line argument and converts it to an integer.
#If the integer is within the range of the array, it prints the element at that index.
#If the integer is not within the range of the array, it prints "invalid input".
#
#*/


import sys

def main():
    array = [1, 2, 3, 4, 5]
    index = int(sys.argv[1])
    if index >= 0 and index < len(array):
        print(array[index])
    else:
        print("invalid input")

if __name__ == "__main__":
    main()