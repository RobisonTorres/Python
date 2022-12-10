print('Building a calculator.')

def calculator(a, b, c):
    if b == ('+'):
        r = a + c
        return r
    elif b == ('-'):
        r = a - c
        return r
    elif b == ('*'):
        r = a * c
        return r
    elif b == ('/'):
        r = a / c
        return r

print(calculator(56, '+', 4))

