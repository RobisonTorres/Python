from math import sqrt, isqrt
print('From Code Wars')

def find_next_square(sq):

    # Given an integer 'sq', it returns -1 for no square numbers,\
    # and the next square number otherwise.
    return -1 if sqrt(sq) != isqrt(sq) else (sqrt(sq) + 1) ** 2

print(find_next_square(25))  # Outputs - 36
print(find_next_square(26))  # Outputs - -1
