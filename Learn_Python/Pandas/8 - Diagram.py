import pandas as pd
import matplotlib.pyplot as plt
print('Pandas')
print()

my_csv = pd.read_csv('data.csv')
print(my_csv.to_string())
# Pandas uses the plot() method to create diagrams.
my_csv.plot()
plt.show()

# Specify that you want a scatter plot with the kind argument:
my_csv.plot(kind='scatter', x='Duration', y='Calories')
plt.show()

# A scatterplot where there are no relationship between the columns:
my_csv.plot(kind='scatter', x='Duration', y='Maxpulse')
plt.show()

# Use the kind argument to specify that you want a histogram:
# A histogram shows us the frequency of each interval, e.g.
# how many workouts lasted between 50 and 60 minutes?
my_csv['Duration'].plot(kind='hist')
plt.show()
