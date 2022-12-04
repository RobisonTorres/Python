print('Working with if statement and comparisons')
print()
def greater(number_1, number_2, number_3):
    if number_1 >= number_2 and number_1 >= number_3:
        print('The first number is the greater.')
    elif number_2 >=- number_1 and number_2 >= number_3:
        print('The second number is the greater')
    elif number_3 >= - number_1 and number_3 >= number_1:
        print('The third number is the greater')
    else:
        print('Nothing here.')

a = float(input('Please, type in the first number: '))
b = float(input('Please, type in the second number: '))
c = float(input('Please, type in the third number: '))

greater(a, b, c)
print('Well done!')
