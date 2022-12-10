print('W3 School')
print()

# this_set = set(('Apple', 'Cherry', 'Banana', 'Banana'))  # Set constructor.
this_set = {'Apple', 'Cherry', 'Banana', 'Banana'}
print(this_set)
this_set.add('Orange')
tropical = ('Mango', 'Coconut', 'Pineapple')
this_set.update(tropical)
set_to_list = list(this_set)  # It is also possible to do this in tuple.
set_to_list.insert(0, 'Papaya')
new_set = set(set_to_list)
print(new_set)
new_set.remove('Mango')
new_set.discard('Melon')  # Even though we don't have 'Melon' in our list,\
# this will not raise an error.
print(new_set)
'''
new_set.clear()
del new_set
'''