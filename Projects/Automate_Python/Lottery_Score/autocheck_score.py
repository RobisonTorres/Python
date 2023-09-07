import sys
sys.path.append(r'C:\Users\rcssi\Code\Python\Python\Projects\Automate_Python\Image_Reader')
from reader_numbers import read_nums
from checking_score import score

def get_numbers():

    # This function retrieves numbers from image and processes them to form lottery games. 
    your_games = []   
    numbers_retrieve = read_nums(f'games.png')
    games_retrieve =  numbers_retrieve.replace('#', ' ').split()
    
    for x in range(0, len(games_retrieve)):
        nums = [n for n in games_retrieve[x]][1:]  # The first number is the n° of the game.   
        numbers = [int(nums.pop(0))]

        while len(numbers) < 15:
            if int(nums[0]) > max(numbers):
                numbers.append(int(nums[0]))
                nums = nums[1:]
            else:
                numbers.append(int(''.join(nums[0:2])))            
                nums = nums[2:]
        your_games.append(numbers)

    return your_games

def auto_check():

    # This function checks the total score hit in each game.
    your_games = get_numbers()
    for n, game in enumerate(your_games, 1):
        print(f'{str(n)} ° Game - {("-".join(map(str, game)))}')
    print()

    lottery_result = score(your_games)
    return lottery_result

print(auto_check())