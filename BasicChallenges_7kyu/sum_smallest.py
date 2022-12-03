print('From Code Wars')
print()

def sum_two_smallest_numbers(numbers):

    # This function will sum two smallest numbers of an array.
    numbers.sort()
    return sum(numbers[:2])
    # return sum(sorted(numbers)[:2]) - clever.

print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))  # Outputs - 7
