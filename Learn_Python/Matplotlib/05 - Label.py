import matplotlib.pyplot as plt
import numpy as np
print('Matplotlib')
print()

# Create Labels for a Plot - With Pyplot, you can use the
# xlabel() and ylabel() functions to set a label for the x- and y-axis.
# You can also use the title() function to set a title for the plot.

# Add labels to the x- and y-axis:
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burned")
plt.show()
