from sklearn.tree import DecisionTreeClassifier

# Input data
X_train = [[1, 2], [2, 3], [3, 4], [4, 5]]
y = [0, 0, 1, 1]
X_val = [[2, 4], [1, 3], [3, 5]]

# Create the decision tree classifier with CART algorithm
clf = DecisionTreeClassifier(random_state=0)

# Train the model using the input data
clf.fit(X_train, y)
predictions = clf.predict(X_val)
predictions
