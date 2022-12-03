print('From Code Wars')
print()

def round_to_next5(n):

    # This function will round any given number
    # to the next number multiple of 5.
    while n % 5 != 0:
        n += 1
    return n
    # return n + (5 - n) % 5 - Clever.

print(round_to_next5(2))  # Outputs - 5
print(round_to_next5(30))  # Outputs - 30
