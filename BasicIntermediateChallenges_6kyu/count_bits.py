print('From Code Wars.')
print()

def count_bits(n):

    # This function counts the number of bits equal to one.
    return sum([1 if a == '1' else 0 for a in f'{bin(n)[2:]}'])
    # return bin(n).count("1") - Clever.

print(count_bits(1234))  # Outputs - 5
