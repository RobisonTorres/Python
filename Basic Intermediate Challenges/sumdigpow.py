print('From Code Wars.')
print()

def sum_dig_pow(a, b):

    # Property: 89 = 8^1 + 9^2, 135 = 1^1 + 3^2 + 5^3
    # Given a range of numbers (a, b), 
    # this function collects numbers that fulfills the property described above.
    numbers = []
    for x in range(a, b+1):
        d = 1
        n = 0
        while d <= len(str(x)):
            n += int(str(x)[-1+d])**d
            d += 1
        if x == n:
            numbers.append(x)
    return numbers
    #  return [x for x in range(a, b+1) if sum([int(d)**i for i, d in enumerate(str(x), 1)]) == x]

print(sum_dig_pow(1, 1000))  # Outputs - [1, 2, 3, 4, 5, 6, 7, 8, 9, 89, 135, 175, 518, 598]
