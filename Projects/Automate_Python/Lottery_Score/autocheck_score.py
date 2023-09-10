import sys, re, checking_score
sys.path.append(r'C:\Users\rcssi\Code\Python\Python\Projects\Automate_Python\Image_Reader')
import reader_numbers

def get_numbers():

    # This function retrieves numbers from image and processes them to form lottery games. 
    your_games = []   
    numbers_retrieved = reader_numbers.read_nums(f'games3.png')
    round_retrieved = re.sub(r'(#\d+)|(\@)', '', numbers_retrieved)
    games_retrieved =  re.sub(r'(#\d)|(\@\d+)', ' ', numbers_retrieved).split()
   
    for x in range(0, len(games_retrieved)):
        nums = [int(n) for n in games_retrieved[x]]   
        numbers = [nums.pop(0)]

        while len(numbers) < 15:
            numbers.append(nums.pop(0) if (nums[0]) > numbers[-1]
                                       else int(str(nums.pop(0)) + str(nums.pop(0))))
        your_games.append(numbers)   

    return [your_games, round_retrieved]

def auto_check():

    # This function checks the total score hit in each game.
    image_result = get_numbers()
    your_games = image_result[0]
    round = image_result[1]

    for n, game in enumerate(your_games, 1):
        print(f'{str(n)}° Game - {("-".join(map(str, game)))}')
    print()   

    lottery_result = checking_score.score(your_games, round)
    return lottery_result

print(auto_check())