import numpy as np

def soft_thresholding(x, threshold):
    if x > threshold:
        return x - threshold
    elif x < -threshold:
        return x + threshold
    else:
        return 0.0

def coordinate_descent_lasso(X, y, regularization_param, tolerance=1e-4, max_iterations=1000):
    n_samples, n_features = len(X), len(X[0])
    coefficients = [0.0 for _ in range(n_features)]
    prev_coefficients = [0.0 for _ in range(n_features)]

    for _ in range(max_iterations):
        for j in range(n_features):
            # Update the j-th coefficient
            X_j = np.array([X[i][j] for i in range(n_samples)])
            y_pred_except_j = np.dot(X, coefficients) - coefficients[j] * X_j
            c_j = np.dot(X_j, y - y_pred_except_j) / np.dot(X_j, X_j)

            # Apply L1 regularization (Lasso) to update the coefficient
            coefficients[j] = soft_thresholding(c_j, regularization_param)

        # Check for convergence
        if np.linalg.norm(np.array(coefficients) - np.array(prev_coefficients)) < tolerance:
            break

        prev_coefficients = coefficients.copy()

    return coefficients.tolist()

# Input data
X = [[1, 1], [1, 2], [1, 3], [1, 4]]
y = [3, 4, 5, 6]
regularization_param = 0.1
tolerance = 0.001

# Train the linear regression model with Lasso regularization using coordinate descent
coefficients = coordinate_descent_lasso(X, y, regularization_param, tolerance)

# Print the result
print("Optimized coefficients:", coefficients)
