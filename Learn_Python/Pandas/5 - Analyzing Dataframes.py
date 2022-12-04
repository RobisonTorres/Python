import pandas as pd
print('Pandas')
print()

# The head() method returns the headers and a specified
# number of rows, starting from the top.

my_csv = pd.read_csv('data.csv')
print(my_csv.head(10))

# The tail() method returns the headers and a specified
# number of rows, starting from the bottom.
print(my_csv.tail(10))

# The DataFrames object has a method called info(), that
# gives you more information about the data set.
print(my_csv.info())

# The DataFrames object has a method called describe(), that
# gives you statical information about the data set.
print(my_csv.describe())  # Very useful.
