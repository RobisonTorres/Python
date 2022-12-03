print('From Code Wars.')
print()

def duplicate_count(text):

    # This function counts how many items have duplicates.
    text = text.lower()
    return sum([1 if num > 1 else 0 for num in\
                [text.count(a) for a in set(text)]])

print(duplicate_count('aabbcde'))  # Outputs - 2
