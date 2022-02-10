# ---------------------------------------- #
# study notes:
# chapter 3 of aurelian geron's book
# ROC curve
# ---------------------------------------- #

#%%

#%% 
from random import Random
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.linear_model import SGDClassifier

import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_predict

mnist = fetch_openml("mnist_784", version=1)
X, y = mnist["data"].values, mnist["target"].values

y = y.astype(np.uint8)
X_train, X_test, y_train, y_test = X[:60_000], X[60_000:], y[:60_000], y[60_000:]

y_train_5 = (y_train == 5)
y_test_5 = (y_test == 5)

sgd_clf = SGDClassifier(random_state=42)
sgd_clf.fit(X_train, y_train_5)

y_scores = sgd_clf.decision_function(X_train)

#%%
from sklearn.metrics import roc_curve
fpr, tpr, thresholds = roc_curve(y_train_5, y_scores)

def plot_roc_curve(fpr, tpr, label=None):
    plt.plot(fpr, tpr, linewidth=2, label=label)
    plt.plot([0,1], [0,1], "k--")

#%%
plot_roc_curve(fpr, tpr)
plt.show()

#%%

from sklearn.metrics import roc_auc_score
roc_auc_score(y_train_5, y_scores)
# 0.9709618248430906

#%%

from sklearn.ensemble import RandomForestClassifier

forest_clf = RandomForestClassifier(random_state=42)
y_probas_forest = cross_val_predict(forest_clf, X_train, y_train_5, cv=3, method="predict_proba")

#%%
y_scores_forest = y_probas_forest[:, 1]
fpr_forest, tpr_forest, thresholds_forest = roc_curve(y_train_5, y_scores_forest)

#%%
plt.plot(fpr, tpr, "b:", label="SGD")
plot_roc_curve(fpr_forest, tpr_forest, "Random Forest")
plt.legend(loc="lower right")
plt.show()

#%%
roc_auc_score(y_train_5, y_scores_forest)
# 0.9983436731328145
#%%

forest_clf.fit(X_train, y_train_5)

y_predict_forest = forest_clf.predict(X_test)

from sklearn.metrics import precision_score, recall_score

precision_score(y_test_5, y_predict_forest)
# 0.993581514762516
recall_score(y_test_5, y_predict_forest)
# 0.8677130044843049
