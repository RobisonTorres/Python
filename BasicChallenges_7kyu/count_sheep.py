print('If you can\'t sleep, just count sheep!!')
print()

def count_sheep(n):

    # This function will count the amount of sheep based in any given number.
    return ''.join([str(number) + ' sheep...' for number in range(1, n+1)])

print(count_sheep(3))  # Outputs - 1 sheep...2 sheep...3 sheep...
