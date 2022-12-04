print('Building a calculator.')

a = float(input('Type in any number: \n '))
x = input('Which operation do you want to do?\n\n'
          'Addition (+)\nSubtraction (-)\nMultiplication (*)\n'
          'Division (/)\nPower (**)\n').capitalize()
c = float(input('Type in any number: '))

if x == ('+'):
    r = a + c
    print(r)
elif x == ('-'):
    r = a - c
    print(r)
elif x == ('*'):
    r = a * c
    print(r)
elif x == ('/'):
    r = a / c
    print(r)
elif x == ('**'):
    r = a ** c
    print(r)
else:
    print('Error!')
