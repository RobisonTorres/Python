print('From Code Wars.')
print()

def split_the_bill(x):

    # This function splits a bill and shows how much each
    # person should pay or receive depending on their spent.
    total_divided = sum(x.values()) / len(x)
    if total_divided % 1 == 0:
        new_values = [num - int(total_divided) for num in x.values()]
    else:
        new_values = [round((num - total_divided), 2) for num in x.values()]
    return dict(zip(x.keys(), new_values))

print(split_the_bill({'A': 20, 'B': 15, 'C': 10}))
# Outputs - {'A': 5, 'B': 0, 'C': -5}
