import pandas
from sklearn import tree
import graphviz
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
print('Machine Learning')
print()

'''
Decision Tree - In this chapter we will show you how to make a 
"Decision Tree". A Decision Tree is a Flow Chart, and can help you 
make decisions based on previous experience. In the example, 
a person will try to decide if he/she should go to a comedy show or not.
'''
df = pandas.read_csv('show1.csv')
# print(x.to_string())
# Now, based on this data set, Python can create a decision tree
# that can be used to decide if any new shows are worth attending to.

'''
To make a decision tree, all data has to be numerical.
We have to convert the non numerical columns 'Nationality' and 'Go' 
into numerical values. Pandas has a map() method that takes a
dictionary with information on how to convert the values.
{'UK': 0, 'USA': 1, 'N': 2}
Means convert the values 'UK' to 0, 'USA' to 1, and 'N' to 2.
'''
# Change string values into numerical values:
d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)
# print(df)

'''
Then we have to separate the feature columns from the target column.
The feature columns are the columns that we try to predict from, 
and the target column is the column with the values we try to predict.
'''

# X is the feature columns, y is the target column:
features = ['Age', 'Experience', 'Rank', 'Nationality']
X = df[features]
y = df['Go']
# print(X)
# print(y)

# Now we can create the actual decision tree, fit it with our details,
# and save a .png file on the computer: Create a Decision Tree, save it
# as an image, and show the image:
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('mydecisiontree.png')
img=pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show()
