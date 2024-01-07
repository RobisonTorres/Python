print('From Code Wars')
print()

def add_binary(a, b):

    # This function sums two numbers (a, b),\
    # and return the result in binary as str.
    return f'{bin(a + b)[2:]}'
    # Bin converts decimal to binary.
    # return format(a + b, 'b') - clever.

print(add_binary(1, 1))  # Outputs - 10
print(add_binary(5, 9))  # Outputs - 1110
