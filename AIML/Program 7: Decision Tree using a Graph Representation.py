import numpy as np
import pydotplus
from sklearn.tree import export_graphviz
from IPython.display import Image

def visualize_decision_tree(tree, feature_names, class_names):
    dot_data = export_graphviz(tree, out_file=None,
                               feature_names=feature_names,
                               class_names=class_names,
                               filled=True, rounded=True,
                               special_characters=True)

    graph = pydotplus.graph_from_dot_data(dot_data)
    return graph

# Example decision tree (output from the previous code)
decision_tree = {'feature_index': 0,
                 'threshold': 3,
                 'left': {'class': 0},
                 'right': {'class': 1}}

# Input data
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([0, 0, 1, 1])
feature_names = ['Feature 1', 'Feature 2']
class_names = ['Class 0', 'Class 1']

# Visualize the decision tree
graph = visualize_decision_tree(decision_tree, feature_names, class_names)
Image(graph.create_png())
