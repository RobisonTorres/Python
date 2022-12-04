print('3W School.')
print()
dictionary = {'Brand': 'Ford',
              'Model': 'Mustang',
              'Year': '2000',
              'Colors': {'Red', 'Bleu', 'Black', 'Purple', 'Green', 'Magenta'}
}
'''
[print(values) for values in dictionary]

for values in dictionary:
    print(dictionary[values])

for x in dictionary.values():
    print(x)
    
for values in dictionary.keys():
    print(values)
'''

for key, value in dictionary.items():
    print(key, value)
