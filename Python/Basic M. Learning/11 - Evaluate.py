import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
print('Machine Learning')
print()

'''
What is Train/Test - Train/Test is a method to measure the accuracy
of your model. It is called Train/Test because you split the data
set into two sets: a training set and a testing set. 80% for training,
and 20% for testing.
'''
# Start with a data set you want to test.
# Our data set illustrates 100 customers in a shop, and their shopping habits.
numpy.random.seed(2)
x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x
plt.scatter(x, y)
plt.show()

# Split Into Train/Test - The training set should be a random selection
# of 80% of the original data. The testing set should be the remaining 20%.
train_x = x[:80]
train_y = y[:80]
test_x = x[80:]
test_y = y[80:]

# Display the same scatter plot with the training set:
plt.scatter(train_x, train_y)
plt.show()  # It looks like the original data set, so it seems to
# be a fair selection.

# To make sure the testing set is not completely different,
# we will take a look at the testing set as well.
plt.scatter(test_x, test_y)
plt.show()  # The testing set also looks like the original data set.

# Draw a polynomial regression line through the data points:
mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
myline = numpy.linspace(0, 6, 100)
plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()

# Remember R2, also known as R-squared? - It measures the relationship
# between the x axis and the y axis, and the value ranges from 0 to 1,
# where 0 means no relationship, and 1 means totally related.
r2 = r2_score(train_y, mymodel(train_x))
print(r2)  # Note: The result 0.799 shows that there is a OK relationship.

# Now we want to test the model with the testing data as well, to see if
# gives us the same result. Let us find the R2 score when using testing data:
r2 = r2_score(test_y, mymodel(test_x))
print(r2)  # The result 0.809 shows that the model fits the testing set as
# well, and we are confident that we can use the model to predict future values.

# Predict Values - Now that we have established that our model is OK,
# we can start predicting new values.
# How much money will a buying customer spend, if she or he stays in
# the shop for 5 minutes?
print(mymodel(5))
