import numpy as np
from sklearn.cluster import DBSCAN

def density_based_clustering(X, epsilon, min_samples):
    # Initialize the DBSCAN clustering algorithm
    dbscan = DBSCAN(eps=epsilon, min_samples=min_samples)
    
    # Perform clustering and get the cluster labels
    cluster_labels = dbscan.fit_predict(X)
    
    return cluster_labels

# Input data
X = np.array([[1, 2], [2, 3], [10, 12], [11, 13], [20, 25], [22, 24]])

# Parameters for DBSCAN (epsilon and min_samples)
epsilon = 3
min_samples = 2

# Perform density-based clustering using the DBSCAN algorithm
cluster_labels = density_based_clustering(X, epsilon, min_samples)

# Print the output
print("Cluster Labels:", cluster_labels.tolist())
