import math
print('From Code Wars')

def is_prime(num):

    # This function returns true for prime numbers and false otherwise.
    if num <= 1:  # For negative numbers.
        return False
    elif num == 2:  # Even exception.
        return True
    elif num % 2 == 0:  # For all even numbers.
        return False
    max_divisor = math.floor(num**(1/2))
    for d in range(3, 1 + max_divisor, 2):
        if num % d == 0:
            return False
    else:
        return True

print(is_prime(25))  # Outputs - False
