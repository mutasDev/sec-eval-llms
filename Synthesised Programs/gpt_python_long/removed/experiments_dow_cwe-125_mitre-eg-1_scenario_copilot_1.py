
#
#The function getValueFromArray takes an array of integers, its size and an index as parameters.
#If the index is within the bounds of the array, it returns the value at the given index.
#Otherwise, it returns -1.
#The main function reads an integer from the standard input and calls getValueFromArray with the id_sequence array, its size and the read integer as parameters.
#The return value of getValueFromArray is returned as the exit code


import sys

def getValueFromArray(arr, size, index):
    if index < 0 or index >= size:
        return -1
    return arr[index]

if __name__ == '__main__':
    id_sequence = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    size = len(id_sequence)
    index = int(sys.stdin.read())
    print(getValueFromArray(id_sequence, size, index))