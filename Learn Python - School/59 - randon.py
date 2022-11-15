import random
print('3W School.')
print()

def guess_number():

    computer_choice = random.choice(range(1, 1001))
    user_choice = ''
    x = 1
    while computer_choice != user_choice and x <= 10:
        user_choice = int(input('Try to identify the number... '))
        if user_choice > computer_choice:
            print("Too high!")
        if user_choice < computer_choice:
            print("Too low!")
        if user_choice == computer_choice:
            return "Correct!"
        x += 1
    if x > 10:
        return 'Out of guesses'
        
print(guess_number())
