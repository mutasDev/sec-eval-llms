
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

def get_value_at_index(index):
    if index < 0:
        return -1
    if index >= len(array):
        return -1
    return array[index]
