print('Working with If statement.')
print()

is_male = True
is_tall = False

if is_male and is_tall:
    print('You are male or tall or both')
elif is_male and not is_tall:
    print('You are male but you are not tall')
elif not is_male and is_tall:
    print('You are not male but you are not tall')
else:
    print('You are neither male nor tall')
