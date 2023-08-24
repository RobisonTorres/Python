print('From Code Wars')
print()

def binary_array_to_number(arr):

    # This function converts a binary number to a decimal.
    return int(''.join([str(num) for num in arr]), 2)  # The method 'int' converts
    # a binary to its decimal value, with base two.

print(binary_array_to_number([1, 0, 0, 0]))  # Outputs - 8 (decimal)

# Binary integers are the number represented with base two.
# Which means in the binary number system,
# there are only two symbols used to represent numbers: 0 and 1.
# Furthermore, there are no more symbols left.
# You do not go to the digit 2 because 2 doesn't exist in binary.
# Instead, you use a special combination of 1s and 0s.
# In a binary system, 1000 is equal to 8 in decimal.
