import pandas as pd
print('Pandas')
print()

my_csv = pd.read_csv('dirtydata.csv')
# Duplicate rows are rows that have been registered more than one time.

# To discover duplicates, we can use the duplicated() method.
# The duplicated() method returns a Boolean values for each row:

# Returns True for every row that is a duplicate, othwerwise False:
print(my_csv.duplicated())

# Removing Duplicates - To remove duplicates, use the drop_duplicates() method.
my_csv.drop_duplicates(inplace=True)
print(my_csv)  # The row 12 has been removed.

# Remember: The (inplace = True) will make sure that the
# method does NOT return a new DataFrame, but it will remove
# all duplicates from the original DataFrame (Not File).
