import random
import numpy as np

def linear_regression_sgd(X, y, learning_rate=0.01, batch_size=1, num_iterations=1000, regularization_term=0.0):
    n_samples, n_features = len(X), len(X[0])

    # Initialize coefficients with zeros
    coefficients = [0.0 for _ in range(n_features)]

    for _ in range(num_iterations):
        # Shuffle the data and create mini-batches
        data = list(zip(X, y))
        random.shuffle(data)
        mini_batches = [data[i:i+batch_size] for i in range(0, n_samples, batch_size)]

        for mini_batch in mini_batches:
            X_batch, y_batch = zip(*mini_batch)
            X_batch, y_batch = np.array(X_batch), np.array(y_batch)

            # Compute the gradient of the loss function with respect to the coefficients
            y_pred = X_batch.dot(coefficients)
            error = y_pred - y_batch
            gradient = X_batch.T.dot(error) / batch_size

            # Add regularization to the gradient (excluding the intercept term)
            gradient[1:] += (regularization_term * coefficients[1:]) / batch_size

            # Update the coefficients using the learning rate and gradient
            coefficients -= learning_rate * gradient
    return coefficients.tolist()
# Input data
X = [[1, 1], [1, 2], [1, 3], [1, 4]]
y = [3, 4, 5, 6]
learning_rate = 0.01
batch_size = 2
num_iterations = 1000
regularization_term = 0.1

# Train the linear regression model using stochastic gradient descent
coefficients = linear_regression_sgd(X, y, learning_rate, batch_size, num_iterations, regularization_term)

# Print the result
print("Optimized coefficients:", coefficients)
