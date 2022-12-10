import pandas as pd
print('Pandas')
print()

# Empty cells can potentially give you a wrong result
# when you analyze data.

my_csv = pd.read_csv('dirtydata.csv')
new_my_csv = my_csv.dropna()
# Note: By default, the dropna() method returns a new
# DataFrame, and will not change the original.
print(my_csv)
print(new_my_csv.to_string())

# If you want to change the original DataFrame, use the
# inplace = True argument:
# my_csv.dropna(inplace=True)

# The fillna() method allows us to replace empty cells with a value:
my_csv.fillna(130, inplace=True)

# To only replace empty values for one column,
# specify the column name for the DataFrame:
my_csv['Calories'].fillna(130, inplace=True)

# Calculate the Mean, and replace any empty values with it:
x = my_csv['Calories'].mean()
my_csv['Calories'].fillna(x, inplace=True)

# Calculate the Median, and replace any empty values with it:
x = my_csv['Calories'].median()
my_csv['Calories'].fillna(x, inplace=True)

# Calculate the Mode, and replace any empty values with it:
x = my_csv['Calories'].mode()
my_csv['Calories'].fillna(x, inplace=True)
