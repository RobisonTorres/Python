print('From Code Wars.')
print()

def expanded_form(num):

    # This function writes any given number in its expanded form.
    nums = []
    num = str(num)
    while num:
        nums.append(num[0] + '0' * len(num[1:]))
        num = num[1:]
    return ' + '.join([n for n in nums if not n.startswith('0')])

print(expanded_form(70304))  # Outputs - 70000 + 300 + 4
