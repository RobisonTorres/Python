import numpy
print('From Code Wars.')
print()
def persistence(n):

    # This function takes in a positive parameter 'n' and
    # returns its multiplicative persistence, which is the number of times
    # you must multiply the digits in 'n' until you reach a single digit.
    cycle = 0
    while len(str(n)) > 1:
        n = numpy.prod([int(num) for num in str(n)])
        cycle += 1
    return cycle

print(persistence(56))  # Outputs - 2 Times.
