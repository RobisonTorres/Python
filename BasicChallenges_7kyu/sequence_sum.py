print('From Code Wars')
print()

def sequence_sum(begin_number, end_number, step):

    # This function returns the sum of a sequence of integers.
    return sum([n for n in range(begin_number, end_number + 1, step)])
    # return sum(range(start, end+1, step)) - Clever.

print(sequence_sum(2, 2, 2))  # Outputs - 2
print(sequence_sum(2, 6, 2))  # Outputs - 12
