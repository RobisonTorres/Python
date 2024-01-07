print('From Code Wars.')
print()

def narcissistic(value):

    # This function determines if a number is or not narcissistic.
    return value == sum([int(n)**len(str(value)) for n in str(value)])

print(narcissistic(153))  # Outputs - True - 01 + 125 + 27 = 153
print(narcissistic(370))  # Outputs - True - 27 + 343 + 00 = 370
