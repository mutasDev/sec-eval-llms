
#
#The code above is a function that takes in an index value and returns the value at that index in the array id_sequence. If the index value is out of bounds, the function returns -1.
#
#The function is called in the main function. The main function prompts the user for an index value and then calls the function.
#
#The function returns the value at the index in the array id_sequence. If the index is out of bounds, the function returns -1


def main():
    index = int(input("Enter an index value: "))
    print(id_sequence(index))

def id_sequence(index):
    id_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    if index < 0 or index > 9:
        return -1
    else:
        return id_sequence[index]

main()