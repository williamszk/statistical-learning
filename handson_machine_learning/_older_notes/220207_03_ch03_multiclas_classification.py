# ---------------------------------------- #
# study notes:
# chapter 3 of aurelian geron's book
# Multiclass Classification
# ---------------------------------------- #
#%%
from random import Random
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.linear_model import SGDClassifier
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_predict, cross_val_score
 
mnist = fetch_openml("mnist_784", version=1) # <=== takes a long time to run...
X, y = mnist["data"].values, mnist["target"].values
y = y.astype(np.uint8)
X_train, X_test, y_train, y_test = X[:60_000], X[60_000:], y[:60_000], y[60_000:]
y_train_5 = (y_train == 5)
y_test_5 = (y_test == 5)
#%%

from sklearn.svm import SVC
svm_clf = SVC()
svm_clf.fit(X_train, y_train) # <=== takes a long time to run...

some_digit = X_test[0]
svm_clf.predict([some_digit])

#%%
some_digit_scores = svm_clf.decision_function([some_digit])
some_digit_scores
some_digit_scores.shape

np.argmax(some_digit_scores)
svm_clf.classes_
svm_clf.classes_[7]

#%%
# let's use a smaller dataset to run this example for quick results
X_train, X_test, y_train, y_test = X[:6_000], X[6_000:7_000], y[:6_000], y[6_000:7_000]

from sklearn.multiclass import OneVsRestClassifier
ovr_clf = OneVsRestClassifier(SVC())
ovr_clf.fit(X_train, y_train)

ovr_clf.predict([some_digit])

len(ovr_clf.estimators_)

#%%

sgd_clf = SGDClassifier(random_state=42)
sgd_clf.fit(X_train, y_train)
sgd_clf.predict([some_digit])

sgd_clf.decision_function([some_digit])
# array([[ -537496.85204195, -1269721.0056062 ,  -167737.67653879,
#           -30478.53756439,  -459903.89685906,  -473041.94711441,
#          -970955.48022674,   451422.55958625,  -177416.61316326,
#          -250988.50158435]])
dir(sgd_clf)
sgd_clf.classes_
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=uint8)

#%%
from sklearn.ensemble import RandomForestClassifier
forest_clf = RandomForestClassifier(random_state=42)
forest_clf.fit(X_train, y_train)
forest_clf.predict([some_digit])


#%%
from sklearn.model_selection import cross_val_score
cross_val_score(sgd_clf, X_train, y_train, cv=3, scoring="accuracy")
# array([0.8565, 0.8715, 0.8635])


#%%

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train.astype(np.float64))
cross_val_score(sgd_clf, X_train_scaled, y_train, cv=3, scoring="accuracy")
# array([0.8705, 0.8985, 0.8925])

