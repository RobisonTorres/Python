print('From Code Wars')
print()

def solution(digits):

    # This function will return the greatest\
    # number of 5 digits within the given number.
    return max([int(digits[i:i + 5]) for i in range(0, len(digits))])

print(solution('1234567890'))  # Outputs - 67890
