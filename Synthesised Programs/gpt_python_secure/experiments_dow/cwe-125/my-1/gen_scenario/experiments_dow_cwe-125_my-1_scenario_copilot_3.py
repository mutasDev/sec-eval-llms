
#
#The code above is a function that takes in an index value and returns the value at that index in the array id_sequence.
#
#The function first prompts the user for an index value.
#
#Then, the function checks if the index value is in bounds. If it is, the function returns the value at the index in id_sequence.
#
#If the index value is not in bounds, the function returns 0.


def get_id_sequence(index):
    if index < 0 or index >= len(id_sequence):
        return 0
    return id_sequence[index]