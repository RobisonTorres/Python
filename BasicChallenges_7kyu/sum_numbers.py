print('From Code Wars')
print()

def get_sum(a, b):

    # This function sums all numbers between a and b, including them.
    # If the two numbers are equal it should returns a or b.
    return sum([num for num in range(min(a, b), max(a, b)+1)])

print(get_sum(1, 2))  # Outputs - 3
