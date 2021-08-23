# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np


# %%
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)


# %%
import matplotlib.pyplot as plt
import numpy as np


# %%
plt.plot(X,y, ".")


# %%
X_b = np.c_[np.ones((100, 1)), X] # add x0 = 1 to each instance
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)


# %%
theta_best


# %%
X_new = np.array([[0], [2]])
X_new


# %%
X_new_b = np.c_[np.ones((2, 1)), X_new]
X_new_b


# %%
y_predict = X_new_b.dot(theta_best)
y_predict


# %%
plt.plot(X_new, y_predict, "r-")
plt.plot(X, y, "b.")
plt.axis([0, 2, 0, 15])
plt.show()


# %%
from sklearn.linear_model import LinearRegression


# %%
lin_reg = LinearRegression()


# %%
lin_reg.fit(X, y)


# %%
lin_reg.intercept_, lin_reg.coef_


# %%
lin_reg.predict(X_new)


# %%
y_pred = lin_reg.predict(X)


# %%
plt.plot(X,y_pred, ".")


# %%
theta_best_svd, residuals, rank, s = np.linalg.lstsq(X_b, y, rcond=1e-6)


# %%
theta_best_svd


# %%
np.linalg.pinv(X_b).dot(y)


# %%
eta = 0.1 # learning rate
n_iterations = 1000
m = 100


# %%
theta = np.random.randn(2,1) # random initialization


# %%
theta


# %%
for iteration in range(n_iterations):
    gradients = 2/m * X_b.T.dot(X_b.dot(theta) - y)
    theta = theta - eta * gradients


# %%
theta


# %%
n_epochs = 50
t0, t1 = 5, 50 # learning schedule hyperparameters


# %%
def learning_schedule(t):
    return t0 / (t + t1)


# %%
theta = np.random.randn(2,1) # random initialization


# %%
for epoch in range(n_epochs):
    for i in range(m):
        random_index = np.random.randint(m)
        xi = X_b[random_index:random_index+1]
        yi = y[random_index:random_index+1]
        gradients = 2 * xi.T.dot(xi.dot(theta) - yi)
        eta = learning_schedule(epoch * m + i)
        theta = theta - eta * gradients


# %%
theta


# %%
from sklearn.linear_model import SGDRegressor


# %%
sgd_reg = SGDRegressor(max_iter=1000, tol=1e-3, penalty=None, eta0=0.1)


# %%
sgd_reg.fit(X, y.ravel())


# %%
y.ravel()


# %%
sgd_reg.fit(X, y.ravel())


# %%
sgd_reg.intercept_, sgd_reg.coef_


# %%



# %%
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn as sns
sns.set()


# %%
m = 100
X = 6 * np.random.rand(m, 1) - 3
y = 0.5 * X**2 + X + 2 + np.random.randn(m, 1)


# %%
plt.plot(X,y,".")


# %%
from sklearn.preprocessing import PolynomialFeatures
poly_features = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly_features.fit_transform(X)
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X_poly, y)
lin_reg.intercept_, lin_reg.coef_


# %%
X_new = np.linspace(-3,3,num=50).reshape(-1, 1)
X_new2 = poly_features.transform(X_new)
y_new =lin_reg.predict(X_new2)


# %%
plt.plot(X,y,".")
plt.plot(X_new, y_new, "r-")
plt.axis([-3.5, 4, -1, 10])
plt.show()


# %%



# %%



# %%
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn as sns
sns.set()
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import SGDRegressor


# %%
m = 100
X = 6 * np.random.rand(m, 1) - 3
y = 0.5 * X**2 + X + 2 + np.random.randn(m, 1)


# %%
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

def plot_learning_curves(model, X, y):
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)
    train_errors, val_errors = [], []
    for m in range(30, len(X_train)):
        model.fit(X_train[:m], y_train[:m])
        y_train_predict = model.predict(X_train[:m])        
        y_val_predict = model.predict(X_val)
        train_errors.append(mean_squared_error(y_train[:m], y_train_predict))
        val_errors.append(mean_squared_error(y_val, y_val_predict))
        
    plt.plot(np.sqrt(train_errors), "r-+", linewidth=2, label="train")
    plt.plot(np.sqrt(val_errors), "b-", linewidth=3, label="val")


# %%
lin_reg = LinearRegression()
plot_learning_curves(lin_reg, X, y)


# %%
from sklearn.pipeline import Pipeline

polynomial_regression = Pipeline([
("poly_features", PolynomialFeatures(degree=10, include_bias=False)),
("lin_reg", LinearRegression()),
])


# %%
plot_learning_curves(polynomial_regression, X, y)


# %%
from sklearn.linear_model import Ridge

ridge_reg = Ridge(alpha=1, solver="cholesky")


# %%
ridge_reg.fit(X, y)


# %%
ridge_reg.predict([[1.5]])


# %%



# %%
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn as sns
sns.set()
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import SGDRegressor


# %%
sgd_reg = SGDRegressor(penalty="l2")
sgd_reg.fit(X, y.ravel())
sgd_reg.predict([[1.5]])


# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



