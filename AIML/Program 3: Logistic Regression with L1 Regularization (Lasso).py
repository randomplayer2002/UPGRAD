import numpy as np
from sklearn.linear_model import LogisticRegression

X = [[1, 2], [2, 3], [3, 4], [4, 5]]
y = [0, 0, 1, 1]
regularization_param = 0.1
tolerance = 0.001

def logistic_regression_with_l1_regularization(X, y, regularization_param, tolerance):
    # Create the Logistic Regression model with L1 regularization
    model = LogisticRegression(penalty='l1', C=1/regularization_param, tol=tolerance, solver='liblinear', random_state=0)
    
    # Train the model
    model.fit(X, y)
    return model

model = logistic_regression_with_l1_regularization(X, y, regularization_param, tolerance)

model.coef_
