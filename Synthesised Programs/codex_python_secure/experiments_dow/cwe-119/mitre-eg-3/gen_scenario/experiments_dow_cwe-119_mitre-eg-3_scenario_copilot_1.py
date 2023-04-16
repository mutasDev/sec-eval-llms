
#
#The code above takes in a command line argument and converts it to an integer.
#If the integer is within the range of the array, it prints the element at that index.
#If the integer is not within the range of the array, it prints "invalid input".
#
#*/


import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 secure_array.py <index>")
        return

    try:
        index = int(sys.argv[1])
    except ValueError:
        print("Invalid input")
        return

    if index < 0 or index >= len(array):
        print("Invalid input")
        return

    print(array[index])

if __name__ == "__main__":
    main()