print('Building a Guessing Game.')
print()

secret_word = 'Gateway'
guess = ''
guess_count = 0

while guess != secret_word and guess_count < 3:
    guess = input('Enter the guess word: ')
    guess_count = guess_count + 1

if guess != secret_word:
    print('You lose.')
else:
    print('Well Done!')
