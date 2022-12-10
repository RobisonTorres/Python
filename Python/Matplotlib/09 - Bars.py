import matplotlib.pyplot as plt
import numpy as np
print('Matplotlib')
print()

# Draw 4 vertical bars:
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
# The bar() takes the keyword argument width to set the width of the bars:
plt.bar(x, y, width=0.2)
plt.show()

# If you want the bars to be displayed horizontally instead
# of vertically, use the barh() function:

# Draw 4 horizontal bars:
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
# The barh() takes the keyword argument height to set the height of the bars:
plt.barh(x, y, color='red', height=0.1)
plt.show()
