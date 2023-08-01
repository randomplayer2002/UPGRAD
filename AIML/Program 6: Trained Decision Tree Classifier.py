import numpy as np

def predict_sample(sample, tree):
    if 'class' in tree:
        return tree['class']

    feature_index = tree['feature_index']
    threshold = tree['threshold']

    if sample[feature_index] < threshold:
        return predict_sample(sample, tree['left'])
    else:
        return predict_sample(sample, tree['right'])

def predict(X_new, tree):
    return [predict_sample(sample, tree) for sample in X_new]

# Example decision tree (output from the previous code)
decision_tree = {'feature_index': 0,
                 'threshold': 3,
                 'left': {'class': 0},
                 'right': {'class': 1}}

# Input data for prediction
X_new = np.array([[1, 3], [1, 4], [2, 3]])

# Predict class labels using the trained decision tree classifier
predicted_labels = predict(X_new, decision_tree)

print("Predicted class labels:", predicted_labels)
