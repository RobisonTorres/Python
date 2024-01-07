print('From Code Wars.')
print()

def wave(people):

    # This function turns a string into a Mexican Wave.
    x = 0
    arr = []
    while x < len(people):
        if people[x] == " ":
            x += 1
        else:
            arr.append(people[0:x] + people[x].upper() + people[x+1:])
            x += 1
    return arr
    # return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]

print(wave(" gap "))  # Outputs - [' Gap ', ' gAp ', ' gaP ']
