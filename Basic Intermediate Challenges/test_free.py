print('Test Free - keep it clean')
print()

def wave(people):

    x = 1
    arr = [people.capitalize()]
    while x < len(people):
        if people[x] != " ":
            x += 1
        else:
            x += 2
        arr.append(people[0:x] + people[x].upper() + people[x+1:])
    return arr

print(wave("Two words"))

# ['Two words', 'tWo words', 'twO words', 'two Words', 'two wOrds', 'two woRds', 'two worDs', 'two wordS']
