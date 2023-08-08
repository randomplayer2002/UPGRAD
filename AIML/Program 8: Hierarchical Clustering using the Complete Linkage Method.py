import numpy as np
from sklearn.cluster import AgglomerativeClustering

# Input data
X = np.array([[1, 2], [2, 3], [10, 12], [11, 13], [20, 25], [22, 24]])

# Perform hierarchical clustering using complete linkage
clustering = AgglomerativeClustering(linkage='complete')
clustering.fit(X)

# Get the cluster assignments for each data point
labels = clustering.labels_
labels
