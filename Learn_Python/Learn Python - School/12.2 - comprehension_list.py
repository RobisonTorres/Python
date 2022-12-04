print('W3 School.')
print()

fruits = list(('Apple', 'Banana', 'Cherry', 'Kiwi', 'Mango', 'Orange'))
# new_list = []
'''Example - Based on a list of fruits, you want a new list, containing 
only the fruits with the letter 'a' in the name'''

'''
for x in fruits:
    if 'a' in x.lower():
        new_list.append(x)
'''

# list comprehension - shorter syntax
new_list = [item for item in fruits if 'a' in item]
'''
new_list = [item for item in fruits] - if statement is optional.
print(fruits)
print(new_list)
number = [x for x in range(10)]  # 10 it is not included.
number = [x for x in range(10) if x % 2]  # 10 it is not included.
print(number)
fruits_up = [x.upper() for x in fruits]
print(fruits_up)
'''
number_even = [x for x in range(10) if x % 2 == 0]  # 10 it is not included.
number_odd = [x for x in range(10) if x % 2 == 1]
print(number_even)
print(number_odd)

to_hello = ['hello' for x in fruits]  # You can set the outcome to whatever you like.
print(to_hello)

list_numbers = [1, 2, 3]
def even_odd(arr):
    return ['even' if num % 2 == 0 else 'odd' for num in arr]

print(even_odd(list_numbers))