
#
#The code above is a function that takes in an index value and returns the value at that index in the array id_sequence. If the index value is out of bounds, the function returns -1.
#
#The function is called in the main function. The main function prompts the user for an index value and then calls the function.
#
#The function returns the value at the index in the array id_sequence. If the index is out of bounds, the function returns -1


def get_value_at_index(index):
    if index < 0 or index >= len(id_sequence):
        return -1
    return id_sequence[index]

def main():
    index = int(input("Enter an index: "))
    value = get_value_at_index(index)
    if value == -1:
        print("Index out of bounds")
    else:
        print("Value at index", index, "is", value)

main()