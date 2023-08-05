X = [[1, 1], [1, 2], [1, 3], [1, 4]]
y = [3, 4, 5, 6]
learning_rate = 0.01
batch_size = 2
num_iterations = 1000
regularization_term = 0.1
random_state=42
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler

def train_linear_regression(X, y, learning_rate, batch_size, regularization_term, max_iterations):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    model = SGDRegressor(loss='squared_error',learning_rate='constant',eta0=learning_rate,alpha=regularization_term,max_iter=max_iterations,tol=1e-3,random_state=0)
    n_samples = X_scaled.shape[0]
    for iteration in range(max_iterations):
        start_idx = 0
        while start_idx < n_samples:
                end_idx = start_idx + batch_size
                X_batch = X_scaled[start_idx:end_idx]
                y_batch = y[start_idx:end_idx]
                model.partial_fit(X_batch, y_batch)
                start_idx = end_idx

    return model

model = train_linear_regression(X,y,learning_rate, batch_size ,regularization_term ,num_iterations)

model.coef_
