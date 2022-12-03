print('From Code Wars')
print()

def sum_digits(number):

    # This function returns the sum of the absolute digits
    # from any given number.
    return sum((int(num) for num in str(abs(number))))

print(sum_digits(-523))  # Outputs - 10
print(sum_digits(-105))  # Outputs - 6
