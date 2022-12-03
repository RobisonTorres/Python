print('From Code Wars')
print()

def divisors(integer):

    # This function returns the divisors of any given number,
    # or the number itself if it's prime number.
    a = [num for num in range(2, integer) if integer % num == 0]
    return a if len(a) != 0 else f'{integer} is prime.'
    # An empty list equals to false.

print(divisors(12))  # Outputs - [2, 3, 4, 6]
print(divisors(13))  # Outputs - 13 is prime.
