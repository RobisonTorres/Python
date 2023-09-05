import checking_score
import sys
sys.path.append(r'your_path\Automate_Python\Image_Reader')
from reader_num import read_nums

def get_numbers():

    # This function...   
    numbers_image = read_nums('game1.png')

    nums = [n for n in numbers_image]
    numbers = [0]

    while nums:
        if int(nums[0]) > max(numbers):
            numbers.append(int(nums[0]))
            nums = nums[1:]
        else:
            numbers.append(int(''.join(nums[0:2])))            
            nums = nums[2:]

    game = numbers[1:]
    show_result = '-'.join(['0' + str(n) if len(str(n)) == 1 else str(n) for n in game])
    print(f'Your game: {show_result}\n')

    result = checking_score.score([game])
    return result

print(get_numbers())
