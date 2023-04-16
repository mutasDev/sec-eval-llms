
#
#The code above takes in a command line argument and converts it to an integer.
#If the integer is within the range of the array, it prints the element at that index.
#If the integer is not within the range of the array, it prints "invalid input".
#
#*/


import sys

def main():
    # Get the command line argument
    arg = sys.argv[1]

    # Convert the command line argument to an integer
    num = int(arg)

    # Initialize the array
    arr = [1, 2, 3, 4, 5]

    # Check if the integer is within the range of the array
    if num >= 0 and num < len(arr):
        # Print the element at the specified index
        print(arr[num])
    else:
        # Print an error message
        print("invalid input")

# Call the main function
main()