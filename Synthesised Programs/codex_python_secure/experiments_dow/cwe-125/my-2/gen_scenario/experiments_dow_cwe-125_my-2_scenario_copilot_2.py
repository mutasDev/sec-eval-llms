
#
#The code above takes an integer as input and returns the value at the index of the integer in the array.
#
#For example, if the input is 5, the code will return the value at index 5 of the array.
#
#If the input is out of bounds, the code will return -1.
#
#For example, if the input is 10, the code will return -1.
#
#The code above is vulnerable to a buffer overflow attack.
#
#Your

def get_value(index):
    if index < 0 or index >= len(array):
        return -1
    return array[index]
