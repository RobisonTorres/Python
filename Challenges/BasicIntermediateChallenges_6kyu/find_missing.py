print('From Code Wars.')
print()

def find_missing_letter(chars):

    # This function returns the missing letter in a array.
    p = [ord(num) - 96 for num in chars]
    m = chr([n for n in list(range(p[0], p[-1] + 1)) if n not in p][0] + 96)
    return m

print(find_missing_letter(['a', 'b', 'c', 'd', 'f']))  # Outputs - 'e'
