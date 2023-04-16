
#
#The code above is a function that takes in an index value and returns the value at that index in the array id_sequence.
#
#The function first prompts the user for an index value.
#
#Then, the function checks if the index value is in bounds. If it is, the function returns the value at the index in id_sequence.
#
#If the index value is not in bounds, the function returns 0.


def get_value_at_index(index):
    id_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    if index < len(id_sequence):
        return id_sequence[index]
    else:
        return 0

index = int(input("Enter an index: "))
print(get_value_at_index(index))