import matplotlib.pyplot as plt
import numpy as np
print('Matplotlib')
print()

# With the subplot() function you can draw multiple plots in one figure:
'''
The subplot() function takes three arguments that describes 
the layout of the figure. The layout is organized in rows 
and columns, which are represented by the first and second argument.
The third argument represents the index of the current plot.
'''

# You can add a title to each plot with the title() function:

# plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(1, 2, 1)  # The figure has 1 row, 2 columns,
# and this plot is the first plot.
plt.plot(x, y)
plt.title("Sales")

# plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(1, 2, 2)  # # The figure has 1 row, 2 columns,
# and this plot is the second plot.
plt.plot(x, y)
plt.title("Income")

# You can add a title to the entire figure with the suptitle() function:
plt.suptitle("My Shop")
plt.show()

# You can draw as many plots you like on one figure, just descibe
# the number of rows, columns, and the index of the plot.
