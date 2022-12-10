from sklearn.preprocessing import StandardScaler
import pandas
print('Machine Learning')
print()

'''
When your data has different values, and even different measurement units, 
it can be difficult to compare them. What is kilograms compared to meters?
Or altitude compared to time? The answer to this problem is scaling. 
We can scale data into new values that are easier to compare.

It can be difficult to compare the volume 1.0 with the weight 790, 
but if we scale them both into comparable values, we can easily see how 
much one value is compared to the other.
You do not have to do this manually, the Python sklearn module has a 
method called StandardScaler() which returns a Scaler object with methods
for transforming data sets.
'''
# Scale all values in the Weight and Volume columns:
scale = StandardScaler()
df = pandas.read_csv("cars2.csv")
X = df[['Weight', 'Volume']]
scaledX = scale.fit_transform(X)
print(scaledX)
