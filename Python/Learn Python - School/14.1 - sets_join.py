print('W3 School')
print()

a = {'Apple', 'Cherry', 'Banana', 'Banana'}
b = {'Car', 'Home', 'Bus', 'Pedestrian'}
c = ('Mango', 'Coconut', 'Pineapple', 'Apple')  # Tuple
d = ['Garden', 'Park', 'Shopping Mall', 'Pedestrian']  # List

# Here I'm combining list, tuple and sets, and \
# it could be any iterable when using 'update' or 'join' methods.

a.update(c)  # It inserts all item from one iterable to a set.
print(a)
print(a.issuperset(c))
new_set = b.union(d)  # It combines two or more iterable into a new set.
print(new_set)

brand = {'Microsoft', 'Apple', 'IBM'}
fruit = {'Apple', 'Banana', 'Cherry'}

'''
# Using intersection_update.

brand.intersection_update(fruit)  # This method will keep only the items \
# that are present in both sets.
print(brand)

or in a different way with a new variable using intersection().

neo_set = brand.intersection(fruit)
print(neo_set)

equals to {'Apple'}
'''
'''
# Using symmetric_difference_update.

brand.symmetric_difference_update(fruit)  # This method will keep only the items \
# that are not present in both sets.
print(brand)
'''

# or in a different way with a new variable using symmetric_difference().

neo_set = brand.symmetric_difference(fruit)
print(neo_set)

# equals to {'Banana', 'Microsoft', 'IBM', 'Cherry'}
