print('From Code Wars.')
print()

def rev_rot(string, sz):
    
    '''
    (...) If a chunk represents an integer such as the sum of the cubes of its digits is 
    divisible by 2, reverse that chunk; otherwise rotate it to the left by one position.
    Put together these modified chunks and return the result as a string.
    '''
    if string == '' or sz <= 0 or sz > len(string):
        return ''
    else:
        new = []
        while string:
            new.append(string[0:sz])
            string = string[sz:]
        new = [c for c in new if len(c) == sz]
        numbers = []
        for x in range(len(new)):
            if sum([int(n) for n in new[x]]) % 2 == 0:
                numbers.append(new[x][::-1])
            else:
                numbers.append(new[x][1:] + new[x][0])
        return ''.join(numbers)

print(rev_rot("66443875", 4))  # Outputs - 44668753
