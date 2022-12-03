print('From Code Wars')
print()

def remove_smallest(numbers):

    # This function will remove the smallest number from an array,\
    # without altering the original array.
    new = numbers.copy()
    if len(new) > 0:
        new.remove(min(new))
    return new

print(remove_smallest([3, 3, 4, 5, 1, 1]))  # Outputs - [3, 3, 4, 5, 1]
print(remove_smallest([]))  # Outputs - []

# if new: - Empty list equals to False.
    # new.remove(min(new))
