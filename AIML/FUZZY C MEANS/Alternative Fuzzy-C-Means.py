import numpy as np
import skfuzzy as fuzz

# Input data
X = np.array([[1, 2], [2, 3], [10, 12], [11, 13], [20, 25], [22, 24]])

# Number of clusters
c = 3

# Fuzzy C-means clustering
cntr, u, _, _, _, _, _ = fuzz.cluster.cmeans(
    X.T, c, m=2.0, error=1e-6, maxiter=1000
)

# Extract cluster centers
cluster_centers = cntr.T

# Print cluster centers
print("Cluster Centers:", cluster_centers)
