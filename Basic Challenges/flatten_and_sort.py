print('From Code Wars')
print()

def flatten_and_sort(array):

    # This function takes a 2D array, and return a  flatten
    # version with all elements in ascending order.
    return sorted([j for sub in array for j in sub])
    # return sorted(sum(array, [])) - Clever.

print(flatten_and_sort([[1, 3, 5], [100], [2, 4, 6]]))
# Outputs - [1, 2, 3, 4, 5, 6, 100]
