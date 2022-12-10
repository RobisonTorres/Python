import pandas as pd

print('Pandas')
print()

# Create a DataFrame from two Series:

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
my_data = pd.DataFrame(data)

# Pandas use the loc attribute to return one or more specified row(s)
print(my_data.loc[0])  # calories    420 duration     50

Labels = ['Day 1 ', 'Day 2', 'Day 3']

my_data = pd.DataFrame(data, index=Labels)
print(my_data)

# Load a Python Dictionary into a DataFrame:
data1 = {
    "Duration": {
        "0": 60,
        "1": 60,
        "2": 60,
        "3": 45,
        "4": 45,
        "5": 60
    },
    "Pulse": {
        "0": 110,
        "1": 117,
        "2": 103,
        "3": 109,
        "4": 117,
        "5": 102
    },
    "Maxpulse": {
        "0": 130,
        "1": 145,
        "2": 135,
        "3": 175,
        "4": 148,
        "5": 127
    },
    "Calories": {
        "0": 409,
        "1": 479,
        "2": 340,
        "3": 282,
        "4": 406,
        "5": 300
    }
}
my_data_dictionary = pd.DataFrame(data1)
print(my_data_dictionary)

# print(my_data_dictionary.describe())  # Gives all statical information.

print(my_data_dictionary['Maxpulse'].describe())
# It describes only the max pulse column.

certificates_earned = pd.DataFrame({
    'Certificates': [8, 2, 5, 6],
    'Time (in months)': [16, 5, 9, 12]
})

certificates_earned.index = ['Tom', 'Kris', 'Ahmad', 'Beau']
certificates_earned = pd.DataFrame(certificates_earned,
                                   index=certificates_earned.index)
print(certificates_earned.iloc[2])
