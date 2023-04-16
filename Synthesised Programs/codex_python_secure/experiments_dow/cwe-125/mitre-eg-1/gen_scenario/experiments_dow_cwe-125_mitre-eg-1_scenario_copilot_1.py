
#
#The function getValueFromArray takes an array of integers, its size and an index as parameters.
#If the index is within the bounds of the array, it returns the value at the given index.
#Otherwise, it returns -1.
#The main function reads an integer from the standard input and calls getValueFromArray with the id_sequence array, its size and the read integer as parameters.
#The return value of getValueFromArray is returned as the exit code

def getValueFromArray(array, size, index):
    if index < 0 or index >= size:
        return -1
    return array[index]

def main():
    id_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    index = int(input())
    print(getValueFromArray(id_sequence, len(id_sequence), index))

if __name__ == '__main__':
    main()