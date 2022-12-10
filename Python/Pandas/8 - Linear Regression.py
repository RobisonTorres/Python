from scipy import stats
import matplotlib.pyplot as plt
print('Machine Learning')
print()

'''
Regression - The term regression is used when you try to find
the relationship between variables. In Machine Learning, 
and in statistical modeling, that relationship is used to predict 
the outcome of future events.
Linear regression uses the relationship between the data-points 
to draw a straight line through all them.
'''
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]


# Import scipy and draw the line of Linear Regression:
slope, intercept, r, p, std_err = stats.linregress(x, y)

def my_func(n):
    return slope * n + intercept

my_model = list(map(my_func, x))
plt.scatter(x, y)
plt.plot(x, my_model)
plt.show()

'''
Predict Future Values - Now we can use the information we have 
gathered to predict future values. Example: Let us try to predict 
the speed of a 10 years old car. To do so, we need the same my_func() 
function from the example above:
'''

# Predict the speed of a 10 years old car:
speed = my_func(10)
print(speed)  # Outputs - 85.6

print(r)  # Outputs - -0.76 - This number indicates a good relationship.
