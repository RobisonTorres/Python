import pandas as pd
print('Pandas')
print()

# CSV files contains plain text and is a well know format
# that can be read by everyone including Pandas.

my_csv = pd.read_csv('data.csv')
# Tip: use to_string() to print the entire DataFrame.
print(my_csv['Duration'])

# If you have a large DataFrame with many rows, Pandas will
# only return the first 5 rows, and the last 5 rows:
print(my_csv)

print(my_csv.info())  # Info method gives information about the dataframe.

# Increase the maximum number of rows to display the entire DataFrame:
pd.options.display.max_rows = 9999
