print('From Code Wars')
print()

def factorial(n):

    # This function will calculate the factorial of any given
    # number between 1 and 12, and trow an error if the number
    # is not between this interval.
    fac = 1
    if n < 0 or n > 12:
        raise ValueError
    else:
        for num in range(1, n + 1):
            fac *= num
        return fac

print(factorial(12))  # Outputs - 479001600
print(factorial(13))  # Outputs - ValueError
