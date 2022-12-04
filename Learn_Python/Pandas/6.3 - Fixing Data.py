import pandas as pd
print('Pandas')
print()

my_csv = pd.read_csv('dirtydata.csv')
# print(my_csv.to_string())

# One way to fix wrong values is to replace them with something else.
# Pandas use the loc attribute to return one or more specified row(s)
# Set "Duration" = 45 in row 7:

my_csv.loc[7, 'Duration'] = 45
print(my_csv)

# For small data sets you might be able to replace the
# wrong data one by one, but not for big data sets.
# To replace wrong data for larger data sets you can
# create some rules, e.g. set some boundaries for legal
# values, and replace any values that are outside of the boundaries.

# Loop through all values in the "Duration" column.

# If the value is higher than 120, set it to 120:
for x in my_csv.index:
    if my_csv.loc[x, "Duration"] > 120:
        my_csv.loc[x, "Duration"] = 120

# Delete rows where "Duration" is higher than 120:
for x in my_csv.index:
    if my_csv.loc[x, "Duration"] > 120:
        my_csv.drop(x, inplace=True)
