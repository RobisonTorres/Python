import matplotlib.pyplot as plt
import seaborn as sns
print('Numpy')
print()

# Distplot stands for distribution plot, it takes as
# input an array and plots a curve corresponding to the
# distribution of points in the array.
sns.distplot([0, 1, 2, 3, 4, 5])
plt.show()

# Plotting a Distplot Without the Histogram.
sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
plt.show()
