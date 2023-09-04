import sys
sys.path.append(r'your_path\Image_Reader')
from reader_num import read_nums
sys.path.append(r'your_path\Lottery')
from checking_score import score

#print(score())

def get_number():
    
    a = read_nums('game1.png')
    numbers_image = [n for n in a]
    numbers = []
    while len(numbers) <= 15:
              

print(get_number())
