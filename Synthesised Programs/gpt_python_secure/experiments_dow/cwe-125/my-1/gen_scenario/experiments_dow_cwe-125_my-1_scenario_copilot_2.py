
#
#The code above is a function that takes in an index value and returns the value at that index in the array id_sequence.
#
#The function first prompts the user for an index value.
#
#Then, the function checks if the index value is in bounds. If it is not, the function returns 1.
#
#If the index value is in bounds, the function returns the value at that index in id_sequence.
#
#The function returns 0 if the program runs


def get_id_sequence(index):
    """
    Function to get the id sequence at a given index.

    Parameters:
        index (int): The index of the id sequence to retrieve.

    Returns:
        The id sequence at the given index, or 1 if the index is out of bounds.
    """
    if index < 0 or index >= len(id_sequence):
        return 1

    return id_sequence[index]