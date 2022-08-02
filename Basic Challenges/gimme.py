print('From Code Wars')
print()

def gimme(input_array):

    # This function returns the index of the middle number.
    return input_array.index(sorted(input_array)[1])

print(gimme([0, 1, -3]))  # Outputs - index 0
print(gimme([3, 1, 2]))  # Outputs - index 2
