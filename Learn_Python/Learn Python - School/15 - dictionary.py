print('W3 School.')
print()

dictionary = {'Brand': 'Ford',
              'Model': 'Mustang',
              'Year': '1964',
              'Year': '2000',  # Key value with the same name will\
              # over written the previous one.
              # 'Colors': {'Red', 'Bleu', 'Black', 'Purple', 'Green', 'Magenta'}
}
print(dictionary)
print(dictionary['Brand'])
print(dictionary.get('Year'))
print(len(dictionary))
print(type(dictionary))
print(dictionary.keys())
dictionary['Color'] = ['Red', 'Bleu', 'Black', 'Purple', 'Green', 'Magenta']
print(dictionary.keys())
print(dictionary.values())
a = dictionary.items()
print(a)
if 'Model' in dictionary:
    print('Yes! Model is one of the keys in this dictionary.')
dictionary['Year'] = '1950'
print(dictionary)
# There are two ways to add a new key value into a dictionary.
dictionary.update({'Condition': 'Good'})
# dictionary['Condition'] = 'Good'
print(dictionary)
dictionary.pop('Color')  # It removes a specified value.
# Or removing an item using del method.
del dictionary['Model']
dictionary.popitem()  # It will remove the last item in the dictionary.
print(dictionary)
# del dictionary

print(a)