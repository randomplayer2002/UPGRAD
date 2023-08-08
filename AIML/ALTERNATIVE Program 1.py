import numpy as np
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler

X = np.array([[1,1],[1,2],[1,3],[1,4]])
y = np.array([3,4,5,6])

lr,bs,it,rt,rs = 0.01,2,1000,0.1,42
model = SGDRegressor(learning_rate = 'constant',eta0=lr,alpha=rt,max_iter=it,tol=1e-3,random_state=rs)
scaler=StandardScaler()
X_scaled = scaler.fit_transform(X)
for _ in range(it):
    idx = np.random.permutation(len(X))
    for b in range(0,len(X),bs):
        X_batch,y_batch = X_scaled[idx[b:b+bs]],y[idx[b:b+bs]]
        model.partial_fit(X_batch,y_batch)
model.coef_
