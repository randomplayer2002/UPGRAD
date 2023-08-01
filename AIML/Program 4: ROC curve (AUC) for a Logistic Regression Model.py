import numpy as np
from sklearn.metrics import roc_curve, auc

def calculate_auc(y_true, y_pred):
    fpr, tpr, _ = roc_curve(y_true, y_pred)
    auc_score = auc(fpr, tpr)
    return auc_score

# Given true class labels and predicted probabilities
y_true = np.array([0, 1, 1, 0, 1])
y_pred = np.array([0.2, 0.8, 0.6, 0.3, 0.9])

# Calculate AUC
auc_score = calculate_auc(y_true, y_pred)

print(f"AUC: {auc_score:.3f}")
