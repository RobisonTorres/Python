print('From Code Wars')
print()

def divisors(n):

    # This function counts the number of divisors of an integer.
    return len([num for num in range(1, n + 1) if n % num == 0])
    # return sum(1 for i in xrange(1, n + 1) if n % i == 0) - Other way.

print(divisors(4))  # Outputs - [1, 2, 4] - 3
print(divisors(30))  # Outputs - [1, 2, 3, 5, 6, 10, 15, 30] - 8
