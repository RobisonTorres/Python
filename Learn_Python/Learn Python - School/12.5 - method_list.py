print('3W School.')
print()
fruits = list(('apple', 'Banana', 'cherry', 'kiwi', 'mango', 'Orange', 'apple'))
'''
fruits.append('pineapple')
fruits.clear() It removes all the items from the list, but doesn't delete the list.
del fruits - delete the entire list.
new_fruits = fruits.copy()
print(fruits.count('apple'))
print(fruits.index('apple'))
fruits.insert(0, 'melon')
fruits.pop()  # it removes the last one item.
fruits.pop(0)  # in this case, it will remove the first one.
fruits.remove('Banana')
fruits.reverse()
'''
fruits.sort(key=str.lower)
print(fruits)
