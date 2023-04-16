
#
#The code above takes in a number from the user and returns the value at that index in the array.
#
#If the index is out of bounds, the function returns -1.
#
#The code above is vulnerable to a buffer overflow attack.
#
#The code above is vulnerable to a buffer overflow attack because the getIdFromArray function does not check if the index is out of bounds.
#
#If the index is out of bounds, the function will return -1


def getIdFromArray(array, index):
    if index < 0 or index >= len(array):
        return -1
    return array[index]