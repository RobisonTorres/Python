print('From Code Wars.')
print()

def digital_root(n):

    # Given n, take the sum of the digits of n. If that
    # value has more than one digit, continue reducing in
    # this way until a single-digit number is produced.
    while len(str(n)) >= 2:
        n = sum([int(n) for n in str(n)])
    return n

print(digital_root(16))  # Outputs - 7
print(digital_root(942))  # Outputs - 6
