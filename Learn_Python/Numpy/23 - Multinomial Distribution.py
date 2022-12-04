import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random
print('Numpy')
print()

# Multinomial distribution is a generalization of binomial distribution.
# It describes outcomes of multinomial scenarios unlike binomial
# where scenarios must be only one of two. e.g. Blood type of a
# population, dice roll outcome.

# It has three parameters:
# n - number of possible outcomes (e.g. 6 for dice roll).
# pvals - list of probabilities of outcomes
# (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll).
# size - The shape of the returned array.

x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(x)
