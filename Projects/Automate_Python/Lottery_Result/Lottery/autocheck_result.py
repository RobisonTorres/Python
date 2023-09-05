import checking_score
import sys
sys.path.append(r'Your_Path\Automate_Python\Image_Reader')
from reader_numbers import read_nums

def get_numbers():

    # This function...
    your_games = []   
    games = int(input('\nHow many games do you want to check? '))

    for x in range(1, games + 1):
        numbers_image = read_nums(f'game{x}.png')

        nums = [n for n in numbers_image]
        numbers = [0]

        while nums:
            if int(nums[0]) > max(numbers):
                numbers.append(int(nums[0]))
                nums = nums[1:]
            else:
                numbers.append(int(''.join(nums[0:2])))            
                nums = nums[2:]

        your_games.append(numbers[1:])
        show_result = '-'.join(['0' + str(n) if len(str(n)) == 1 else str(n) for n in numbers[1:]])
        print(f'{x}° game: {show_result}')
    print()
    result = checking_score.score(your_games)
    return result

print(get_numbers())
