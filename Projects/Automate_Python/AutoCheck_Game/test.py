import sys
sys.path.append(r'C:\Users\rcssi\Code\Python\Python\Projects\Automate_Python\Image_Reader')
from reader_num import read_nums
sys.path.append(r'C:\Users\rcssi\Code\Python\Python\Projects\Automate_Python\Lottery')
from checking_score import score

a = read_nums('game1.png')
#print(score())
print(a)

