import matplotlib.pyplot as plt
import numpy as np
print('Matplotlib')
print()

# With Pyplot, you can use the pie() function to draw pie charts:

# A simple pie chart:
y = np.array([35, 25, 25, 15])

# The label parameter must be an array with one label for each wedge:
my_labels = ["Apples", "Bananas", "Cherries", "Dates"]

# The startangle parameter is defined with an angle in degrees,
# default angle is 0:

# Pull the "Apples" wedge 0.2 from the center of the pie:
my_explode = [0.2, 0, 0, 0]

plt.pie(y, labels=my_labels, startangle=0, explode=my_explode)

# To add a list of explanation for each wedge, use the legend() function:
# To add a header to the legend, add the title parameter to the legend function.
plt.legend(title='Fruits')
plt.show()
