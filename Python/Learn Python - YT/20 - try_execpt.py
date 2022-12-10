print('Working with try and execpt.')
print()

try:
    division = 10/0
    number = int(input('Enter a number: '))
    print(number)
#except ZeroDivisionError:
    #print('Divided by zero')
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print('Invalid input.')
