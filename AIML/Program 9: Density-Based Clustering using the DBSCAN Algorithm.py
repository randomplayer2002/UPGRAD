from sklearn.cluster import DBSCAN
import numpy as np

# Input data
X = np.array([[1, 2], [2, 3], [10, 12], [11, 13], [20, 25], [22, 24]])
epsilon = 3
min_samples = 2

def perform_dbscan_clustering(X, epsilon, min_samples):
    # Create a DBSCAN object with the specified epsilon and min_samples
    dbscan = DBSCAN(eps=epsilon, min_samples=min_samples)
    
    # Perform clustering on the data
    clustering_labels = dbscan.fit_predict(X)
    
    # Return the clustering labels
    return clustering_labels

# Perform DBSCAN clustering
labels = perform_dbscan_clustering(X, epsilon, min_samples)
labels
