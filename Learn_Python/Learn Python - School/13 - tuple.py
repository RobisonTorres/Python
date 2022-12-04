print('3W School')

my_tuple = ('apple', 'banana', 'cherry')
print(my_tuple)
# One item tuple.
new_tuple = ('pineapple',)  # don't forget to put a comma after the item.
print(type(new_tuple))

# Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a
# list, change the list, and convert the list back into a tuple.

breakfast = tuple(('Bacon', 'Milk', 'Egg'))
breakfast_list = list(breakfast)
print(breakfast_list)
breakfast_list.insert(3, 'Bread')
breakfast_list.append('Ham')
breakfast = tuple(breakfast_list)
print(breakfast)

fruits = (
    'Apple', 'Orange', 'Cherry', 'strawberry', 'grape',
    'papaya', 'pineapple', 'lemon', 'kiwi', 'coconut'
)

# It is also allowed to do these operations in list.

(a, b, *list_remaining) = fruits  # The * will create a list of the remaining values.
print(a)
print(b)
print(list_remaining)  # Don't put * here on the print command.
