import matplotlib.pyplot as plt
import numpy as np
print('Matplotlib')
print()

# Linestyle - You can use the keyword argument linestyle,
# or shorter ls, to change the style of the plotted line:

# Use a dotted line:
y_points = np.array([3, 8, 1, 10])
plt.plot(y_points, linestyle='dotted')
plt.show()

# Use a dash dot line:
y_points = np.array([3, 8, 1, 10])
plt.plot(y_points, ls='-.')
plt.show()

# Set the line color to red:
y_points = np.array([3, 8, 1, 10])
plt.plot(y_points, color='r')
plt.show()

# Line Width - You can use the keyword argument linewidth or
# the shorter lw to change the width of the line.
y_points = np.array([3, 8, 1, 10])
plt.plot(y_points, linewidth='10.5')
plt.show()

# Multiple Lines - You can plot as many lines as you like by
# simply adding more plt.plot() functions:

# Draw two lines by specifying a plt.plot() function for each line:
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
plt.plot(y1)
plt.plot(y2)
plt.show()

'''
You can also plot many lines by adding the points for the 
x- and y-axis for each line in the same plt.plot() function.
(In the examples above we only specified the points on the y-axis, 
meaning that the points on the x-axis got the the default values (0, 1, 2, 3).)
The x- and y- values come in pairs:
'''

# Draw two lines by specifying the x- and y-point values for both lines:
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])
plt.plot(x1, y1, x2, y2)
plt.show()
