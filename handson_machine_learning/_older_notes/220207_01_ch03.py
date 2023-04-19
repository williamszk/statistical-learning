# ---------------------------------------- #
# study notes:
# chapter 3 of aurelian geron's book
# ---------------------------------------- #

#%%
from cProfile import label
import numpy as np
from sklearn.model_selection import cross_val_predict
from sklearn.datasets import fetch_openml
from sklearn.linear_model import SGDClassifier

import matplotlib as mpl
import matplotlib.pyplot as plt

mnist = fetch_openml("mnist_784", version=1)
X, y = mnist["data"].values, mnist["target"].values

#%%
y = y.astype(np.uint8)
X_train, X_test, y_train, y_test = X[:60_000], X[60_000:], y[:60_000], y[60_000:]

y_train_5 = (y_train == 5)
y_test_5 = (y_test == 5)

sgd_clf = SGDClassifier(random_state=42)
sgd_clf.fit(X_train, y_train_5)

#%%

y_scores = cross_val_predict(sgd_clf, X_train, y_train_5, cv=3, method="decision_function")

#%%
from sklearn.metrics import precision_recall_curve
precisions, recalls, thresholds = precision_recall_curve(y_train_5, y_scores)

def plot_precision_recall_vs_threshold(precisions, recalls, thresholds):
    plt.plot(thresholds, precisions[:-1], "b--", label="Precision")
    plt.plot(thresholds, recalls[:-1], "g-", label="Recall")
#%%
plot_precision_recall_vs_threshold(precisions, recalls, thresholds)
plt.show()

#%%



