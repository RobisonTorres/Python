import pandas as pd
print('Pandas')
print()

# Cells with data of wrong format can make it difficult,
# or even impossible, to analyze data.

# Let's try to convert all cells in the 'Date' column into dates.
my_csv = pd.read_csv('dirtydata.csv')
print(my_csv)

my_csv['Date'] = pd.to_datetime(my_csv['Date'])
print(my_csv.to_string())
# As you can see from the result, the date in row 26 was fixed,
# but the empty date in row 22 got a NaT (Not a Time) value,
# in other words an empty value. One way to deal with empty
# values is simply removing the entire row.

# Remove rows with a NULL value in the "Date" column:
new_csv = my_csv.dropna(subset=['Date'])   #, inplace=True)
print(new_csv)  # It drops the row number 22.
