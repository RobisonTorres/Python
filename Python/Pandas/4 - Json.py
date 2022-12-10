import pandas as pd
print('Pandas')
print()

# Big data sets are often stored, or extracted as JSON.
# JSON is plain text, but has the format of an object,
# and is well known in the world of programming, including Pandas.

my_json = pd.read_json('data.json')
print(my_json.to_string())
