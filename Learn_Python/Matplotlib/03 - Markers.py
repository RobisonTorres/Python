import matplotlib.pyplot as plt
import numpy as np
print('Matplotlib')
print()

# Markers - You can use the keyword argument marker to
# emphasize each point with a specified marker:

# Mark each point with a circle:
y_points = np.array([3, 8, 1, 10])
plt.plot(y_points, marker='o')  # o - marker circle
plt.show()

# Format Strings fmt - You can also use the shortcut string
# notation parameter to specify the marker.
# This parameter is also called fmt, and is written with this syntax:
# marker|line|color

# Mark each point with a circle:
y_points = np.array([3, 8, 1, 10])
plt.plot(y_points, 'o:')  # : - dotted line
plt.show()
# Note: If you leave out the line value in the fmt parameter,
# no line will be plotted.

# Mark each point with a circle:
y_points = np.array([3, 8, 1, 10])
plt.plot(y_points, 'o:r')  # r - red color
plt.show()

# Marker Size - You can use the keyword argument markersize
# or the shorter version, ms to set the size of the markers:

# Set the size of the markers to 20:
y_points = np.array([3, 8, 1, 10])
plt.plot(y_points, 'o:b', ms=10)  # ms - size
plt.show()

# Marker Color - You can use the keyword argument markeredgecolor
# or the shorter mec to set the color of the edge of the markers:

# Set the EDGE color to red:
y_points = np.array([3, 8, 1, 10])
plt.plot(y_points, 'o:g', ms=5, mec='b')  # color blue
plt.show()

# You can use the keyword argument markerfacecolor or the
# shorter mfc to set the color inside the edge of the markers:

# Set the FACE color to red:
y_points = np.array([3, 8, 1, 10])

plt.plot(y_points, marker='o', ms=20, mfc='r')  # Face color
plt.show()
