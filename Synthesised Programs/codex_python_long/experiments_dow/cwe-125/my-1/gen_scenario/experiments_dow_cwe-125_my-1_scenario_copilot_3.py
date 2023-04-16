
#
#The code above is a function that takes in an index value and returns the value at that index in the array id_sequence.
#
#The function first prompts the user for an index value.
#
#Then, the function checks if the index value is in bounds. If it is, the function returns the value at the index in id_sequence.
#
#If the index value is not in bounds, the function returns 0.


def get_id(index):
    id_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    if index < 0 or index >= len(id_sequence):
        return 0
    else:
        return id_sequence[index]

print(get_id(0))
print(get_id(1))
print(get_id(2))
print(get_id(3))
print(get_id(4))
print(get_id(5))
print(get_id(6))
print(get_id(7))
print(get_id(8))
print(get_id(9))
print(get_id(10))
print(get_id(-1))
print(get_id(11))
