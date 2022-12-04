print('Working with Exponent Function')
print()

def raise_to_power(base_number, power_number):
    a = base_number ** power_number
    return a

x = float(input('Enter the base number: '))
y = float(input('Enter the power number: '))

print(raise_to_power(x, y))
print('Well done!')
