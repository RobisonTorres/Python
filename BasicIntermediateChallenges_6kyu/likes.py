print('From Code Wars.')
print()

def likes(names):

    # This function doesn't need explanation.
    if len(names) == 0:
        return 'no one likes this'
    if len(names) == 1:
        return f'{names[0]} likes this'
    if len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    if len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    if len(names) >= 3:
        return f'{names[0]}, {names[1]} and {len(names)- 2} others like this'
print(likes([]))  # Outputs - no one likes this
