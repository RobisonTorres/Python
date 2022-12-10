import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random
print('Numpy')
print()

# Zipf distritutions are used to sample data based on zipf's law.
# Zipf's Law: In a collection the nth common term is 1/n times
# of the most common term. E.g. 5th common word in english has
# occurs nearly 1/5th times as of the most used word.

# It has two parameters:
# a - distribution parameter.
# size - The shape of the returned array.

# Draw out a sample for zipf distribution with distribution
# parameter 2 with size 2x3:
x = random.zipf(a=2, size=(2, 3))
print(x)

# Visualization of Zipf Distribution
# Sample 1000 points but plotting only ones with
# value < 10 for more meaningful chart.
x = random.zipf(a=2, size=1000)
sns.distplot(x[x < 10], kde=False)
plt.show()
