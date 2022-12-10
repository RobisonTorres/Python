import matplotlib.pyplot as plt
import numpy as np
print('Matplotlib')
print()

# With Pyplot, you can use the grid() function to
# add grid lines to the plot.

# Add grid lines to the plot:
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burned")
plt.plot(x, y)
plt.grid()
plt.show()

# Display only grid lines for the x-axis:
# plt.grid(axis='x')

# Set Line Properties for the Grid
# plt.grid(color='green', linestyle='--', linewidth=0.5)
