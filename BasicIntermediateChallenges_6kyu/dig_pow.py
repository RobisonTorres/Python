print('From Code Wars.')
print()

def dig_pow(n, p):

    # This function finds a positive integer k, if it exists,\
    # such as the sum of the digits of n taken to the successive\
    # powers of p is equal to k * n.
    result = sum([int(x)**y for x, y in zip(list(str(n)),
                  range(p, len(str(n)) + p))]) / n
    return result if result % 1 == 0 else - 1

print(dig_pow(46288, 3))  # Outputs - k = 51
print(dig_pow(92, 1))  # Outputs - -1
