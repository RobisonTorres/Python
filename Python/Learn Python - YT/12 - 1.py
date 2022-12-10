print('Working with dictionaries.')

months_conversions = {
    1: 'Car',
    2: 'House',
    3: 'Pen',
    4: 'Pencil',
    5: 'Notebook',
    6: 'Laptop',
    7: 'Smartphone',
    8: 'Windows',
    9: 'Clock',
    10: 'Hair',
    11: 'Dictionaries',
    12: 'December',
}

print(months_conversions[7])
print(months_conversions.get(1))
print(months_conversions.get(0, 'Not a valid key.'))
