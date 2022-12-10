print('Working with try and execpt.')
print()

try:
    number = int(input('Enter a number: '))
    print(number)
except ValueError as errr:
    print(errr)

try:
    division = 10/0
except ZeroDivisionError as err:
    print(err)
#except ZeroDivisionError:
    #print('Divided by zero')

