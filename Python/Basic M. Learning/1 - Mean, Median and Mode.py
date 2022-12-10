import numpy as np
from scipy import stats
print('Machine Learning')
print()

# Mean - The average value
# Median - The mid point value
# Mode - The most common value

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
array_speed = np.array(speed)

# Mean
x = np.mean(array_speed)
print(x)

# Median
x = np.median(array_speed)
print(x)

# Mode
x = stats.mode(array_speed)
print(x)
