import numpy as np
from scipy.cluster.hierarchy import linkage, fcluster

def hierarchical_clustering(X, threshold, method='complete'):
    # Calculate the distance matrix using the complete linkage method
    distance_matrix = linkage(X, method=method)
    
    # Perform hierarchical clustering and get the cluster labels
    cluster_labels = fcluster(distance_matrix, threshold, criterion='distance')
    
    return cluster_labels

# Input data
X = np.array([[1, 2], [2, 3], [10, 12], [11, 13], [20, 25], [22, 24]])

# Threshold for forming clusters (you can adjust this value as needed)
threshold = 5

# Perform hierarchical clustering using the complete linkage method
cluster_labels = hierarchical_clustering(X, threshold, method='complete')

# Print the output
print("Cluster Labels:", cluster_labels.tolist())
