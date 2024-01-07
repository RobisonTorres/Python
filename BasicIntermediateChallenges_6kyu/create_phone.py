print('From Code Wars.')
print()

def create_phone_number(n):

    # This function creates a phone number.
    num = ''.join([str(num) for num in n])
    return f'({num[0:3]}) {num[3:6]}-{num[6:]}'
    # return "({}{}{}) {}{}{}-{}{}{}{}".format(*n) - Clever.

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
# Outputs - (123) 456-7890
