print('From Code Wars')
print()

def find(n):

    # This function will return the sum of all multiples of 3 and 5,\
    # of any given number.
    return [num for num in range(1, n + 1) if num % 3 == 0 or num % 5 == 0]

print(find(5))  # Outputs - 8 [3, 5]
print(find(10))  # Outputs - 33 [3, 5, 6, 9, 10]
