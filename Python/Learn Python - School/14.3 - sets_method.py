print('W3 School')
print()

set_a = {'Apple', 'Cherry', 'Banana', 'Mango'}  # This set also has the Coconut value.
set_b = {'Pineapple', 'Melon', 'Kiwi', 'Coconut'}
set_a.add('Coconut')
# set_a.clear()
that_set = set_a.copy()
set_c = set_a.difference(set_b)
'''
Without variable.

set_a.difference_update(set_b)
'''
a = {'Apple', 'Cherry', 'Banana', 'Cherry'}
b = {'Car', 'Home', 'Bus', 'Pedestrian', 'Space', 'Cherry'}
# b.discard('Space')
# c = a.intersection(b)
# a.intersection_update(b)
# c = a.isdisjoint(b)  # I don't know why this gives me a false statement.
c = a.union(b)
# print(a.issubset(c))
# print(c.issuperset(a))
# popped = c.pop()  # Every time a hit the button run \
# the pop method will remove a random value.
# c.remove('Bus')
# d = a.symmetric_difference(b)  # It will only get the values not equal in both sets.
# a.symmetric_difference_update(b)
a.update(b)
x = set('Ca r')  # This will create a set dividing the characters into one value.\
# It is also allowed to do this operation in tuples and lists.
