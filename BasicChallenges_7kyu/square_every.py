print('From Code Wars.')
print()

def square_digits(num):

    # This function squares every digit from a number and concatenate them.
    return int(''.join([str(n) for n in [int(n)**2 for n in str(num)]]))
    # return int(''.join([str(int(n)**2) for n in str(num)])) - Clever

print(square_digits(9119))  # Outputs = 811181
