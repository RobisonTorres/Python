import pandas as pd
print('Pandas')
print()

list_num = [1, 2, 3]

my_series = pd.Series(list_num)
print(my_series)

# Labels - If nothing else is specified, the values are labeled
# with their index number. First value has index 0, second value has index 1 etc.
# print(my_series[0])  # Output - 1

# With the index argument, you can name your own labels.
Labels = ['x', 'y', 'z']

my_series = pd.Series(list_num, index=Labels)
print(my_series)

# When you have created labels, you can access an item by referring to the label.
# print(my_series['y'])  # Output - 2

# Dictionary - Series
calories = {"day 1": 420, "day 2": 380, "day 3": 390}

my_calories = pd.Series(calories)
print(my_calories)

# Note: The keys of the dictionary become the labels.

# Other example:
certificates_earned = pd.Series(
    [8, 2, 5, 6],
    index=['Tom', 'Kris', 'Ahmad', 'Beau']
)

print(certificates_earned)
# Outputs -
# Tom      8
# Kris     2
# Ahmad    5
# Beau     6
# dtype: int64

print(certificates_earned[certificates_earned > 5])
# Tom     8
# Beau    6
# dtype: int64

# Using the iloc
print(certificates_earned.iloc[2])  # It gets the information using index position
