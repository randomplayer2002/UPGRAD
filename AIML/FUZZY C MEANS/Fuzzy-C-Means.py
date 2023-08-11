import numpy as np
import skfuzzy as fuzz

# Input data
X = np.array([[1, 2], [2, 3], [10, 12], [11, 13], [20, 25], [22, 24]])
c = 3

# Fuzzy C-means clustering
cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(X.T, c, 2, error=0.005, maxiter=1000, init=None)

# u: Cluster membership matrix
# cntr: Cluster centers
# u0: Initial guess of cluster membership
# d: Distance matrix
# jm: Objective function (Fuzzy partition coefficient)
# p: Number of iterations performed
# fpc: Final fuzzy partition coefficient

# Extracting the cluster memberships for each data point
cluster_membership = np.argmax(u, axis=0)

# Print the results
print("Cluster Centers:")
print(cntr)

print("\nCluster Membership Matrix:")
print(u)

print("\nData Point - Cluster Membership:")
for i, data_point in enumerate(X):
    print(f"Data Point {i+1}: Cluster {cluster_membership[i]+1}")


# use pip install -U scikit-fuzzy to install fuzzy package
