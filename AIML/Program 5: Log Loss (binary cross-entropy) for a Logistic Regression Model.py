import numpy as np
from sklearn.metrics import log_loss

# Input data
y_true = np.array([0, 1, 1, 0])
y_pred = np.array([0.2, 0.8, 0.9, 0.3])

# Ensure y_pred is within [epsilon, 1-epsilon] to avoid log(0) and log(1) issues
epsilon = 1e-15

y_pred = np.clip(y_pred, epsilon, 1 - epsilon)

# Calculate the log loss (binary cross-entropy)
logloss = log_loss(y_true, y_pred)
print("Log Loss (Binary Cross-Entropy):", logloss)
