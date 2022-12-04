from chef import Chef
from chineseChef import chinese_chef

print('Working with Inheritance.')
print()

my_chef = Chef()
chinese_chef = chinese_chef()

my_chef.make_special_dish()
chinese_chef.make_special_dish()
my_chef.make_chicken()
chinese_chef.make_fried_rice()
