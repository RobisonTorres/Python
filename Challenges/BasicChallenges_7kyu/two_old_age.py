print('From Code Wars')
print()

def two_oldest_ages(ages):

    # This function will return the two oldest ages from an array.
    return sorted(ages)[-2:]

print(two_oldest_ages([1, 3, 10, 0]))  # Outputs - [3, 10]
print(two_oldest_ages([1, 5, 87, 45, 8, 8]))  # Outputs - [45, 87]
