print('From Code Wars.')
print()

def two_sum(numbers, target):

    # This function finds two different index items in the array that,
    # when added together, give the target value.
    x = 0
    n = ''
    while n not in numbers:
        n = target - numbers[x]
        x += 1
    if numbers.count(n) == 1:
        return x - 1, numbers.index(n)
    else:
        return x - 1, numbers[x:].index(n) + len(numbers[:x])

print(two_sum([1, 2, 2, 3, 3], 4))  # Outputs - (0, 3)
