import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
import numpy as np

# Input data
X = [[1, 2], [2, 3], [3, 4], [4, 5]]
y = [0, 0, 1, 1]

def visualize_decision_tree(X, y):
    # Create the decision tree classifier with CART algorithm
    clf = DecisionTreeClassifier()

    # Train the model using the input data
    clf.fit(X, y)
    
    # Obtain a text representation of the decision tree
    tree_text = export_text(clf, feature_names=[f'Feature {i+1}' for i in range(len(X[0]))])
    print("Decision Tree Text Representation:")
    print(tree_text)
    
    # Create a graphical representation of the decision tree
    plt.figure(figsize=(10, 6))
    plot_tree(clf, filled=True, feature_names=[f'Feature {i+1}' for i in range(len(X[0]))], class_names=['Class 0', 'Class 1'])
    
    plt.show()

# Call the visualization function
visualize_decision_tree(X, y)
