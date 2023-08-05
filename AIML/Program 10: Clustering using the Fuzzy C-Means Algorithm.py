import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Input data
X = np.array([[1, 2], [2, 3], [10, 12], [11, 13], [20, 25], [22, 24]])
k = 3

# Perform k-means clustering
kmeans = KMeans(n_clusters=k, init='k-means++', random_state=0)
y_kmeans = kmeans.fit_predict(X)

# Extract the cluster centers and labels
cluster_centers = kmeans.cluster_centers_
labels = kmeans.labels_
labels
