print('From Code Wars')
print()

def max_multiple(divisor, bound):

    # This function returns the max number module\
    # by the divisor.
    return max([num for num in range(divisor, bound + 1) if num % divisor == 0])
    # return bound - (bound % divisor) - Clever.


print(max_multiple(2, 7))  # Outputs - 6
print(max_multiple(37, 200))  # Outputs - 185
