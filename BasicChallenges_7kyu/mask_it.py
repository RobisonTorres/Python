print('From Code Wars')
print()

def maskify(cc):

    # This function hides sensitive information, like credit card number.
    return '#' * (len(cc) - 4) + cc[-4:] if len(cc) > 4 else cc
    # return '#' * (len(cc) - 4) + cc[-4:] - '-4' will get the # to zero.

print(maskify('1234586914782584'))  # Outputs - ############2584
