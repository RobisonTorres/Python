print('From Code Wars.')
print()

def unique_in_order(iterable):

    # This function takes an iterable and return its items into an array
    # without the same item next to each other.
    try:
        new = [iterable[0]]
        [new.append(a) for a in list(iterable) if a != new[-1]]
        return new
    except:
        return []

print(unique_in_order('AAAABBBCCDAABBB'))  # Outputs - ['A', 'B', 'C', 'D', 'A', 'B']
print(unique_in_order([1, 2, 2, 3, 3]))  # Outputs - [1, 2, 3]
