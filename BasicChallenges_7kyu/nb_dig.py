print('From Code Wars')
print()

def nb_dig(n, d):

    # This function counts the amount of digits (d)\
    # in each square number inside the range of zero to n.
    return sum([str((num**2)).count(str(d)) for num in range(0, n + 1)])

print(nb_dig(1000, 0))  # Outputs - 618
print(nb_dig(10, 1))  # Outputs - 4 {0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100}
