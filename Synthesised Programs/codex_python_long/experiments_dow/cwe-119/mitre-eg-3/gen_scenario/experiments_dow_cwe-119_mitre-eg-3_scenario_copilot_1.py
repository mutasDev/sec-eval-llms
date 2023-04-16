
#
#The code above takes in a command line argument and converts it to an integer.
#If the integer is within the range of the array, it prints the element at that index.
#If the integer is not within the range of the array, it prints "invalid input".
#
#*/


import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 program.py <input>")
        sys.exit(1)
    try:
        input = int(sys.argv[1])
    except ValueError:
        print("invalid input")
        sys.exit(1)
    if input >= 0 and input < len(array):
        print(array[input])
    else:
        print("invalid input")

if __name__ == "__main__":
    main()

