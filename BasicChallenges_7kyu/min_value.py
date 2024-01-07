print('From Code Wars')
print()

def min_value(digits):

    # It returns the smallest number that could be formed from these digits,
    # using the digits only once (ignore duplicates).
    return int(''.join([str(num) for num in sorted(set(digits))]))

print(min_value({5, 7, 5, 9, 7}))  # Outputs - 579
