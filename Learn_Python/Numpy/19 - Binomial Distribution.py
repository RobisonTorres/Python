import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random
print('Numpy')
print()

# Binomial Distribution is a Discrete Distribution.
# It describes the outcome of binary scenarios,
# e.g. toss of a coin, it will either be head or tails.

# It has three parameters:
# n - number of trials.
# p - probability of occurrence of each trial (e.g. for toss of a coin 0.5 each).
# size - The shape of the returned array.

# Given 10 trials for coin toss generate 10 data points:
x = random.binomial(n=10, p=0.5, size=10)
print(x)

# Visualization of Binomial Distribution
sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)
plt.show()

# Difference Between Normal and Binomial Distribution:
# The main difference is that normal distribution is
# continuous whereas binomial is discrete, but if there
# are enough data points it will be quite similar to normal
# distribution with certain loc and scale.

sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
plt.show()
