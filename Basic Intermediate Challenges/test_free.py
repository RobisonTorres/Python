print('Test Free - keep it clean')
print()

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function

    '''
    In effect: 89 = 8^1 + 9^2
    The next number in having this property is 135.
    See this property again: 135 = 1^1 + 3^2 + 5^3
    We need a function to collect these numbers, that may receive two integers 
    a, b that defines the range [a, b] (inclusive) and outputs a list of the sorted
    numbers in the range that fulfills the property described above.
    '''
    numbers = []
    for x in range(a, b+1):
        n = [int(y)+d for y in str(x) for d in range(1, len(y)+1)]
        numbers.append(n)
        '''
        if  x == sum([int(y)**d for y in str(x) for d in range(1, len(y))]):
            numbers.append(x)'''
    return numbers

print(sum_dig_pow(10, 13))  # Outputs - (10, 89),  [89])
