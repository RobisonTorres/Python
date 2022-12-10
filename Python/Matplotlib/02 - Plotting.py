import matplotlib.pyplot as plt
import numpy as np
print('Matplotlib')
print()

'''
The plot() function is used to draw points (markers) in a diagram.
By default, the plot() function draws a line from point to point.
The function takes parameters for specifying points in the diagram.
Parameter 1 is an array containing the points on the x-axis.
Parameter 2 is an array containing the points on the y-axis.
'''
x_points = np.array([1, 8])
y_points = np.array([3, 10])
plt.plot(x_points, y_points)
plt.show()

# Plotting Without Line - To plot only the markers, you can use
# shortcut string notation parameter 'o', which means 'rings'.

# Draw two points in the diagram, one at position (1, 3)
# and one in position (8, 10):
x_points = np.array([1, 8])
y_points = np.array([3, 10])
plt.plot(x_points, y_points, 'o')
plt.show()

# Multiple Points - You can plot as many points as you like,
# just make sure you have the same number of points in both axis.

# Draw a line in a diagram from position (1, 3) to (2, 8)
# then to (6, 1) and finally to position (8, 10):
x_points = np.array([1, 2, 6, 8])
y_points = np.array([3, 8, 1, 10])
plt.plot(x_points, y_points)
plt.show()

# Default X-Points - If we do not specify the points in the x-axis,
# they will get the default values 0, 1, 2, 3,
# (etc. depending on the length of the y-points.

# Plotting without x-points:
y_points = np.array([3, 8, 1, 10, 5, 7])
plt.plot(y_points)
plt.show()
