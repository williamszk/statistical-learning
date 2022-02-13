# ---------------------------------------- #
# study notes:
# chapter 3 of aurelian geron's book
# Error Analysis
# ---------------------------------------- #
#%%

from random import Random
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.linear_model import SGDClassifier
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_predict, cross_val_score
 
mnist = fetch_openml("mnist_784", version=1) # <=== takes a long time to run...
X, y = mnist["data"].values, mnist["target"].values
y = y.astype(np.uint8)

# let's use a smaller dataset to run this example for quick results
X_train, X_test, y_train, y_test = X[:6_000], X[6_000:7_000], y[:6_000], y[6_000:7_000]
# X_train, X_test, y_train, y_test = X[:60_000], X[60_000:], y[:60_000], y[60_000:]

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train.astype(np.float64))

sgd_clf = SGDClassifier(random_state=42)
#%%
y_train_pred = cross_val_predict(sgd_clf, X_train_scaled, y_train, cv=3)
conf_mx = confusion_matrix(y_train, y_train_pred)
conf_mx

# array([[572,   0,   1,   2,   1,   9,   3,   1,   3,   0],
#        [  0, 637,   6,   3,   1,   5,   0,   1,  16,   2],
#        [ 10,  12, 493,  11,  10,   4,  10,   9,  20,   2],
#        [  3,   5,  21, 514,   1,  35,   1,   7,  11,  10],
#        [  3,   2,   7,   0, 556,   2,  10,   8,   9,  26],
#        [  5,   6,   5,  24,  14, 411,  10,   1,  25,  13],
#        [  4,   4,   6,   0,   5,   6, 577,   1,   5,   0],
#        [  3,   4,   7,   2,   9,   0,   1, 577,   3,  45],
#        [  2,  19,  13,  16,   4,  10,   6,   3, 464,  14],
#        [  7,   4,   5,   7,  15,   3,   0,  27,  11, 522]], dtype=int64)

#%%
plt.matshow(conf_mx, cmap=plt.cm.gray)
plt.show()
#%%
row_sums = conf_mx.sum(axis=1, keepdims=True)
norm_conf_mx = conf_mx / row_sums
np.fill_diagonal(norm_conf_mx, 0)
#%%
plt.matshow(norm_conf_mx, cmap=plt.cm.gray)
plt.show()

#%%
cl_a, cl_b = 3, 5
X_aa = X_train[(y_train == cl_a) & (y_train_pred == cl_a)]
X_ab = X_train[(y_train == cl_a) & (y_train_pred == cl_b)]
X_ba = X_train[(y_train == cl_b) & (y_train_pred == cl_a)]
X_bb = X_train[(y_train == cl_b) & (y_train_pred == cl_b)]
#%%
plt.figure(figsize=(8,8))
plt.subplot(221); plot_digits(X_aa[:25], images_per_row=5)
plt.subplot(222); plot_digits(X_ab[:25], images_per_row=5)
plt.subplot(223); plot_digits(X_ba[:25], images_per_row=5)
plt.subplot(224); plot_digits(X_bb[:25], images_per_row=5)
plt.show()
#%%




#%%




#%%




#%%




#%%




#%%




#%%




