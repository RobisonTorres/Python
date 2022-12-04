import numpy
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
print('Machine Learning')
print()

'''
Polynomial Regression - If your data points clearly will not fit 
a linear regression (a straight line through all data points), it
might be ideal for polynomial regression. Polynomial regression,
like linear regression, uses the relationship between the variables
x and y to find the best way to draw a line through the data points.
'''
x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]

my_model = numpy.poly1d(numpy.polyfit(x, y, 3))
my_line = numpy.linspace(1, 22, 100)
plt.scatter(x, y)
plt.plot(my_line, my_model(my_line))
plt.show()

# R-Squared - The r-squared value ranges from 0 to 1, where 0
# means no relationship, and 1 means 100% related.
print(r2_score(y, my_model(x)))  # Outputs - 0.943 - A good relationship.

'''
Predict Future Values - Now we can use the information we have gathered 
to predict future values. Example: Let us try to predict the speed of a 
car that passes the tollbooth at around 17 P.M:
To do so, we need the same my_model array from the example above:
'''
speed = my_model(17)
print(speed)  # Outputs - The example predicted a speed to be 88.87
