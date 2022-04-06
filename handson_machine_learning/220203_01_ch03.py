# ---------------------------------------- #
# study notes:
# chapter 3 of aurelian geron's book
# ---------------------------------------- #

# chapter 3
# Classification

from lib2to3.pytree import Base
from random import random
import numpy as np

from sklearn.datasets import fetch_openml

mnist = fetch_openml("mnist_784", version=1)

#%%

mnist.keys()

print(mnist["DESCR"])

X, y = mnist["data"].values, mnist["target"].values
X.shape
y.shape

#%%
import matplotlib as mpl
import matplotlib.pyplot as plt

#%%
some_digit = X[0]
some_digit_image = some_digit.reshape(28, 28)

plt.imshow(some_digit_image, cmap="binary")
plt.axis("off")
plt.show()

print(y[0])
type(y[0]) # str
y = y.astype(np.uint8)
type(y)
#%%
# split train and test
X_train, X_test, y_train, y_test = X[:60_000], X[60_000:], y[:60_000], y[60_000:]
X_train.shape

#%%
y_train_5 = (y_train == 5)
y_test_5 = (y_test == 5)

#%%
from sklearn.linear_model import SGDClassifier

sgd_clf = SGDClassifier(random_state=42)
sgd_clf.fit(X_train, y_train_5)
#%%
sgd_clf.predict([some_digit])
# true

sgd_clf.predict([X[1]])
# false
y[1]
# 0

#%%
# Cross-validation
from sklearn.model_selection import StratifiedKFold
# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html
from sklearn.base import clone

skfolds = StratifiedKFold(n_splits=3, random_state=42, shuffle=True)

#%%
for train_index, test_index in skfolds.split(X_train, y_train):
    clone_clf = clone(sgd_clf)
    X_train_folds = X_train[train_index]
    y_train_folds = y_train[train_index]
    X_test_folds = X_train[test_index]
    y_test_folds = y_train[test_index]

    clone_clf.fit(X_train_folds, y_train_folds)
    y_pred = clone_clf.predict(X_test_folds)
    n_correct = sum(y_pred == y_test_folds)

    print(n_correct/len(y_pred))

# 0.87155
# 0.8499
# 0.8632

#%%
from sklearn.model_selection import cross_val_score
cross_val_score(sgd_clf, X_train, y_train_5, cv=3, scoring="accuracy")
# array([0.95035, 0.96035, 0.9604 ])
#%%
from sklearn.base import BaseEstimator

class Never5Classifier(BaseEstimator):
    def fit(self, X, y = None):
        return self
    def predict(self, X):
        return np.zeros((len(X), 1), dtype=bool)

#%%
never_5_clf = Never5Classifier()
cross_val_score(never_5_clf, X_train, y_train_5, cv=3, scoring="accuracy")
# array([0.91125, 0.90855, 0.90915])
# skewed datasets..., unbalanced datasets

#%%
# Confusion Matrix

from sklearn.model_selection import cross_val_predict
y_train_pred = cross_val_predict(sgd_clf, X_train, y_train_5, cv=3)
#%%
from sklearn.metrics import confusion_matrix

confusion_matrix(y_train_5, y_train_pred)

#%%

y_train_perfect_predictions = y_train_5
confusion_matrix(y_train_5, y_train_perfect_predictions)

#%%
# Precision and Recall
from sklearn.metrics import precision_score, recall_score
precision_score(y_train_5, y_train_pred)
recall_score(y_train_5, y_train_pred)

from sklearn.metrics import f1_score
f1_score(y_train_5, y_train_pred)

#%%
# Precision Recall Trade Off

y_scores = sgd_clf.decision_function([some_digit])
y_scores
threshold = 0
y_some_digit_pred = (y_scores > threshold)
y_some_digit_pred

