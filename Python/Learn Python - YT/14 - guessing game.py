print('Building a Guessing Game.')
print()

secret_word = 'Gateway'
guess = ''
guess_count = 0
guess_limit = 3
out_of_guessing = False

while guess != secret_word and not out_of_guessing:
    if guess_count < guess_limit:
        guess = input('Enter the guess word: ')
        guess_count = guess_count + 1
    else:
        out_of_guessing = True

if out_of_guessing:
    print('You lose.')
else:
    print('Well Done!')
