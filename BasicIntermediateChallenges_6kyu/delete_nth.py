print('From Code Wars.')
print()

def delete_nth(order, max_e):

    new = []
    [new.append(num) for num in order if new.count(num) < max_e]
    return new

print(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3))
# Outputs - [1, 1, 3, 3, 7, 2, 2, 2]
'''
Task - Given a list and a number, create a new list that contains
each number of list at most N times, without reordering. For example
if the input number is 2, and the input list is [1,2,3,1,2,1,2,3], 
you take [1,2,3,1,2]. 
'''
