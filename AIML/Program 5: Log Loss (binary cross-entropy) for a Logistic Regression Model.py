import numpy as np

def log_loss(y_true, y_pred):
    epsilon = 1e-15  # To prevent log(0) cases
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)  # Clip predictions to avoid log(0) and log(1)
    n = len(y_true)
    loss = -1/n * np.sum(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
    return loss

# Input data
y_true = np.array([0, 1, 1, 0])
y_pred = np.array([0.2, 0.8, 0.9, 0.3])

# Calculate log loss
log_loss_value = log_loss(y_true, y_pred)

print("Log loss:", round(log_loss_value, 3))
