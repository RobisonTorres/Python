import checking_score
import sys
sys.path.append(r'C:\Users\rcssi\Code\Python\Python\Projects\Automate_Python\Image_Reader')
from reader_numbers import read_nums

def get_numbers():

    # This function retrieves numbers from image and processes them to form
    # lottery games. Then it gives the total score hit with each game.
    your_games = []   
    numbers_retrieve = read_nums(f'games1.png')
    games_retrieve =  numbers_retrieve.replace('#', ' ').split()
    
    for x in range(0, len(games_retrieve)):
        nums = [n for n in games_retrieve[x]][1:]  # The first number is the n° of the game.   
        numbers = [0]

        while len(numbers) <= 15:
            if int(nums[0]) > max(numbers):
                numbers.append(int(nums[0]))
                nums = nums[1:]
            else:
                numbers.append(int(''.join(nums[0:2])))            
                nums = nums[2:]

        your_games.append(numbers[1:])
        print(f'{x + 1}° Game: {"-".join([str(n).zfill(2) for n in numbers[1:]])}')
    print()

    lottery_result = checking_score.score(your_games)
    if len(lottery_result) == 1:
        return f'Round: {lottery_result[0]} - Result not found.'

    return lottery_result

print(get_numbers())
