print('From Code Wars.')
print()

def order_weight(strng):

    # This function puts a group of number in ascending
    # order based on the sum of their digits.
    order = sorted([[sum(map(int, list(d))), d] for d in strng.split()])
    order = ' '.join([item[1] for item in order])
    return order

print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))
# Outputs - 11 11 2000 10003 22 123 1234000 44444444 9999
