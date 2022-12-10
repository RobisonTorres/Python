import numpy as np
import matplotlib.pyplot as plt
print('Machine Learning')
print()

'''
Normal Data Distribution - In the previous chapter we learned 
how to create a completely random array, of a given size, and 
between two given values.
In this chapter we will learn how to create an array where the 
values are concentrated around a given value.
'''
# A typical normal data distribution:
x = np.random.normal(5.0, 1.0, 100000)
plt.hist(x, 100)
plt.show()

'''
Histogram Explained - We use the array from the numpy.random.normal() 
method, with 100000 values,  to draw a histogram with 100 bars.
We specify that the mean value is 5.0, and the standard deviation is 1.0.
Meaning that the values should be concentrated around 5.0, and rarely 
further away than 1.0 from the mean.
And as you can see from the histogram, most values are between 4.0 and 6.0, 
with a top at approximately 5.0.
'''
