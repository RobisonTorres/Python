print('From Code Wars')
print()

def in_asc_order(arr):

    # This function determines whether a list is or not in ascending order.
    return arr == sorted(arr)

print(in_asc_order([1, 2, 4, 7, 19]))  # Outputs - True
print(in_asc_order([1, 6, 10, 18, 2, 4, 20]))  # Outputs - False
