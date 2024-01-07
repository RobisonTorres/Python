print('From Code Wars')
print()

def high_and_low(numbers):

    # This function takes a number or a group of numbers as a string,\
    # and return the high and low numbers as a string separated with a whitespace.
    nums = [int(num) for num in numbers.split()]
    return str(max(nums)) + ' ' + str(min(nums))

print(high_and_low("42 0 -125 235 1000"))
# Outputs = 1000 -125
