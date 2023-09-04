import sys
sys.path.append(r'C:\Users\rcssi\Code\Python\Python\Projects\Automate_Python\Image_Reader')
from reader_num import read_nums
sys.path.append(r'C:\Users\rcssi\Code\Python\Python\Projects\Automate_Python\Lottery')
from checking_score import score


def get_numbers():
    
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
    return [numbers[1:]]

#game = get_numbers()
#print(game)
score()
