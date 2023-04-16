
#
#The code above takes an integer as input and returns the value at the index of the integer in the array.
#
#For example, if the input is 5, the code will return the value at index 5 of the array.
#
#If the input is -1, the code will return -1.
#
#If the input is 10, the code will return -1.
#
#If the input is 0, the code will return the value at index 0 of the array


def get_value(arr, index):
    if index < 0 or index >= len(arr):
        return -1
    return arr[index]