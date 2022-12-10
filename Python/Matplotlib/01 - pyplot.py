import matplotlib.pyplot as plt
import numpy as np
print('Matplotlib')
print()

# Pyplot - Most of the Matplotlib utilities lies under the
# pyplot submodule, and are usually imported under the plt alias:

# Draw a line in a diagram from position (0,0) to position (6,250):
x_points = np.array([0, 6])
y_points = np.array([0, 250])
plt.plot(x_points, y_points)
plt.show()
