print('W3 School.')
print()

fruits = list(('Apple', 'Cherry', 'Orange', 'Apple', 'Cherry', 'Orange'))  # Com. list creates a list.
print(type(fruits))  # class list
print(fruits[-1])  # Orange
print(fruits[0:2])  # Apple, Cherry
print(fruits[-4:-1])  # Orange, Apple, Cherry
if 'Cherry' in fruits:
    print('Yes, Cherry is present in the list.')
fruits[1] = 'Banana'  # To change a value inside a list. (Cherry to Banana)
print(fruits)
fruits[1:3] = ['Pen', 'Pall', 'Watermelon']  # To change a range of values.
print(fruits)
# ['Apple', 'Pen', 'Pall', 'Watermelon', 'Apple', 'Cherry', 'Orange']
fruits[1:4] = ['Melon']
print(fruits)
# ['Apple', 'Melon', 'Apple', 'Cherry', 'Orange']
fruits.append('Cherry')  # append method puts a new item on the end of a list.
print(fruits)
# ['Apple', 'Melon', 'Apple', 'Cherry', 'Orange', 'Cherry']
print(len(fruits))
'''
for item in reversed(fruits):
    print(item)
'''
[print(item) for item in fruits]

new_fruits = list(('strawberry', 'grape', 'papaya', 'pineapple', 'lemon'))
print(new_fruits)
fruits.extend(new_fruits)
print(fruits)
# fruits.remove('strawberry')
# print(fruits)
aturple = ('kiwi', 'coconut')
fruits.extend(aturple)
print(fruits)
# ['Apple', 'Melon', 'Apple', 'Cherry', 'Orange', 'Cherry', 'strawberry'
# , 'grape', 'papaya', 'pineapple', 'lemon', 'kiwi', 'coconut']
fruits[1:9] = ['strawberry']
print(fruits)
# ['Apple', 'strawberry', 'pineapple', 'lemon', 'kiwi', 'coconut']
fruits.pop(1)  # It will remove the item in position 1.
print(fruits)
popped = fruits.pop()  # if you do not specify the index the pop method will remove
# the last one on the list.
print(popped)
'''
del fruits[0] # the 'del' also deletes an item.
print(fruits)
del fruits # It deletes the list.
'''
print(fruits)
fruits.clear()  # It clears the list but don't delete it.
print(fruits)  # [] - An empty list.
fruits.insert(0, 'Banana')
print(fruits)
print(fruits.index('Banana'))


num = [1, 2, 2, 3]
num1 = [1, 2, 2, 3]

alpha = []
def is_true(arr, arr1):
    return arr or arr1
print(is_true(num, alpha))
# When you have an empty list it is possible to use the 'or' operator.
print(bool([]))  # False
# An Empty list equals to false.
print(num+num1)
