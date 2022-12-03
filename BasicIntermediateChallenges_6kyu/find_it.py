print('From Code Wars.')
print()

def find_it(seq):

    # This function returns a number from an array \
    # that appears an odd number of times.
    return [n for n in seq if seq.count(n) % 2 != 0][0]

print(find_it([0, 1, 0, 1, 0]))  # Outputs - 0
