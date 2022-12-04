print('W3 School.')
print()

fruits = list(('apple', 'Banana', 'cherry', 'kiwi', 'mango', 'Orange'))
fruits.sort()  # By default the sort method is case sensitive,
# resulting in all capital letters being sorted before lower case letters.
numbers = [60, 70, 50, 5, 6, 18]
numbers.sort()
'''

fruits.sort(reverse=False)
numbers.sort(reverse=True)

def my_function(n):
    return abs(n - 50)  # What's 'abs'?
this_list = [100, 50, 65, 82, 23]
this_list.sort(key=my_function)
print(this_list)

'''

print(fruits)
fruits.sort(key=str.lower)  # Type in this way to have a list case insensitive.
