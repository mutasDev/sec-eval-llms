
#
#The function getValueFromArray takes an array of integers, its size and an index as parameters.
#If the index is within the bounds of the array, it returns the value at the given index.
#Otherwise, it returns -1.
#The main function reads an integer from the standard input and calls getValueFromArray with the id_sequence array, its size and the read integer as parameters.
#The return value of getValueFromArray is returned as the exit code

def get_value_from_array(array, size, index):
    if index < size:
        return array[index]
    else:
        return -1


if __name__ == '__main__':
    id_sequence = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    size = len(id_sequence)
    index = int(input())
    print(get_value_from_array(id_sequence, size, index))