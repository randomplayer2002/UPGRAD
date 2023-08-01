import numpy as np
import skfuzzy as fuzz

def fuzzy_c_means_clustering(X, c):
    # Number of data points
    n_samples = X.shape[0]

    # Number of features
    n_features = X.shape[1]

    # Maximum number of iterations
    max_iter = 1000

    # Fuzziness coefficient (m)
    fuzziness = 2.0

    # Termination threshold
    epsilon = 1e-6

    # Initialize the cluster centers randomly
    cluster_centers = np.random.rand(c, n_features)

    # Perform Fuzzy C-means clustering
    cntr, u, _, _, _, _, _ = fuzz.cluster.cmeans(
        X.T, c, m=fuzziness, error=epsilon, maxiter=max_iter, init=cluster_centers
    )
    return cntr.T

# Input data
X = np.array([[1, 2], [2, 3], [10, 12], [11, 13], [20, 25], [22, 24]])

# Number of clusters (c) for Fuzzy C-means clustering
c = 3

# Perform Fuzzy C-means clustering
cluster_centers = fuzzy_c_means_clustering(X, c)

# Print the output
print("Cluster Centers:", cluster_centers.tolist())
