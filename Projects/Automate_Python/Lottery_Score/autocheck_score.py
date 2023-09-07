import sys, re, checking_score
sys.path.append(r'C:\Users\rcssi\Code\Python\Python\Projects\Automate_Python\Image_Reader')
import reader_numbers

def get_numbers():

    # This function retrieves numbers from image and processes them to form lottery games. 
    your_games = []   
    numbers_retrieve = reader_numbers.read_nums(f'games.png')
    games_retrieve =  re.sub(r'(#\d)', ' ', numbers_retrieve).split() # Remove '#' and the first digit.
    
    for x in range(0, len(games_retrieve)):
        nums = [int(n) for n in games_retrieve[x]]   
        numbers = [nums.pop(0)]

        while len(numbers) < 15:
            numbers.append(nums.pop(0) if (nums[0]) > numbers[-1]
                                       else int(str(nums.pop(0)) + str(nums.pop(0))))
        your_games.append(numbers)
    return your_games

def auto_check():

    # This function checks the total score hit in each game.
    your_games = get_numbers()
    for n, game in enumerate(your_games, 1):
        print(f'{str(n)}° Game - {("-".join(map(str, game)))}')
    print()   
    lottery_result = checking_score.score(your_games)
    return lottery_result

print(auto_check())