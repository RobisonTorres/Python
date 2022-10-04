print('From Code Wars.')
print()

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function

    numbers = []
    for x in range(a, b+1):
        n = [int(y)+d for y in str(x) for d in range(1, len(y)+1)]
        numbers.append(n)
        '''
        if  x == sum([int(y)**d for y in str(x) for d in range(1, len(y))]):
            numbers.append(x)'''
    return numbers

print(sum_dig_pow(10, 13))  # Outputs - (10, 89),  [89])
