print('From Code Wars')
print()

def is_square(n):

    # This function determines if a number is or not a square number.
    num = int((n**(1/2)).real)  # It's necessary to use .real because the int\
                                # conversion gives a complex number.
    return True if n == num * num else False

print(is_square(25))  # Outputs - True
print(is_square(26))  # Outputs - False

# In mathematics, a square number\
# or perfect square is an integer that is the square of an integer;\
# in other words, it is the product (25) of some integer with itself (5 * 5).
