# https://machinelearningmastery.com/automl-libraries-for-python/

# !pip install autosklearn
# ERROR: Could not find a version that satisfies the requirement autosklearn (from versions: none)
# pip install auto-sklearn
# python setup.py egg_info did not run successfully.
# https://appuals.com/command-python-setup-py-egg_info/#:~:text=Fix%3A%20'Command%20%E2%80%9Cpython%20setup,code%201'%20When%20Installing%20Python&text=The%20error%20code%201%20is,to%20be%20installed%20or%20updated.
# pip install --upgrade setuptools
# pip install auto-sklearn
# the same error as previouly occured
# pip install ez_setup
# Try again: pip install auto-sklearn
# did not work...
# 
# 
# 
#  
#%%
# https://automl.github.io/auto-sklearn/master/
# https://arxiv.org/abs/2007.04074

# auto-sklearn relies heavily on the Python module resource. resource is part of Python’s Unix Specific Services and not available on a Windows machine. 
# Therefore, it is not possible to run auto-sklearn on a Windows machine.

# can't run autosklearn in windows machine

#%%

# test tree-based piplie optimization tool (TPOT)
# https://dl.acm.org/doi/10.1145/2908812.2908918
# pip install tpot
# it worked
#%%
from random import random
import tpot
print(f"tpot: {tpot.__version__}")

# example of tpot for a classification dataset
from sklearn.datasets import make_classification
from sklearn.model_selection import RepeatedStratifiedKFold

from tpot import TPOTClassifier

# define dataset
X, y = make_classification(n_samples=100, n_features=10, n_informative=5, n_redundant=5, random_state=1)
X.shape

# define model evaluation
cross_validation = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)

# study: from sklearn.model_selection import RepeatedStratifiedKFold
# What is RepeatedStratifiedKFold?

# define search
model = TPOTClassifier(generations=5, population_size=50, cv=cross_validation, scoring="accuracy", verbosity=2, random_state=1, n_jobs=-1)

# perform the search
model.fit(X, y)

# export the best model
model.export("tpot_best_model.py")

#%%

# below is the code produced by the export above:
# note that the best model is an MLP classifier
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

# NOTE: Make sure that the outcome column is labeled 'target' in the data file
tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR', dtype=np.float64)
features = tpot_data.drop('target', axis=1)
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'], random_state=1)

# Average CV score on the training set was: 0.9399999999999998
exported_pipeline = MLPClassifier(alpha=0.001, learning_rate_init=0.1)
# Fix random state in exported estimator
if hasattr(exported_pipeline, 'random_state'):
    setattr(exported_pipeline, 'random_state', 1)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)

## below is the logging in console:

# Generation 1 - Current best internal CV score: 0.9399999999999998
                                                                              
# Generation 2 - Current best internal CV score: 0.9399999999999998
                                                                              
# Generation 3 - Current best internal CV score: 0.9399999999999998
                                                                              
# Generation 4 - Current best internal CV score: 0.9399999999999998
                                                                              
# Generation 5 - Current best internal CV score: 0.9399999999999998
                                                                              
# Best pipeline: MLPClassifier(input_matrix, alpha=0.001, learning_rate_init=0.1)
# TPOTClassifier(cv=RepeatedStratifiedKFold(n_repeats=3, n_splits=10, random_state=1),
#                generations=5, n_jobs=-1, population_size=50, random_state=1,
#                scoring='accuracy', verbosity=2)

# https://dl.acm.org/doi/10.1145/2908812.2908918
# https://github.com/EpistasisLab/tpot
# https://epistasislab.github.io/tpot/

#%%
# ------------------------------------------------ # # ------------------------------------------------ # 
# Let's test with Hyperopt-Sklearn
# ------------------------------------------------ # # ------------------------------------------------ # 
# https://hyperopt.github.io/hyperopt/
# https://www.linkedin.com/in/james-bergstra/

# !pip install hyperopt

# This too can be installed using pip, although we must perform this operation manually by 
# cloning the repository and running the installation from the local files, as follows:
# cd C:\Users\william.suzuki\Documents
# git clone williamszk@github.com:hyperopt/hyperopt-sklearn.git
# cd hyperopt-sklearn
# pip install .
# cd ..
# the above did not work


# https://github.com/hyperopt/hyperopt-sklearn
# pip install git+https://github.com/hyperopt/hyperopt-sklearn
#%%
from hpsklearn import HyperoptEstimator, svc
from hyperopt import tpe
from sklearn import svm

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, precision_score

use_hpsklearn = True
#%%
# Load Data
# ---
X, y = make_classification(n_samples=100, n_features=10, n_informative=5, n_redundant=5, random_state=1)
X.shape

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
X_train.shape
# ---

if use_hpsklearn:
    estimator = HyperoptEstimator(classifier=svc("mySVC"))
    # AttributeError: 'hyperopt_estimator' object has no attribute 'classifier'
    # https://github.com/hyperopt/hyperopt-sklearn/issues/168
    # solved by including from hyperopt import tpe after import o hpsklearn
    # https://github.com/hyperopt/hyperopt-sklearn/issues/168#issuecomment-799733587
else:
    estimator = svm.SVC()
#%%
# e = HyperoptEstimator(
#     classifier=any_classifier('my_clf'),
#   preprocessing=any_preprocessing('my_pre'),
#   algo=tpe.suggest,
#   max_evals=2,
#   trial_timeout=5)
# # e.get_params()    

estimator.fit(X_train, y_train)
# AttributeError: 'numpy.random.mtrand.RandomState' object has no attribute 'integers'
# https://github.com/maxpumperla/hyperas/issues/284
# https://github.com/maxpumperla/hyperas/issues/284#issuecomment-994247029
# it maybe the hyperopt version problem，please choose other version of hyperopt
# pip install hyperopt==0.2.5
# restart everything, then try again
# 

estimator.score(X_test, y_test)

#%%
# ------------------------------------------------ # # ------------------------------------------------ # 
# Let's test with Hyperopt-Sklearn
# ------------------------------------------------ # # ------------------------------------------------ # 

# example of hyperopt-sklearn for a classification dataset

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

from hpsklearn import HyperoptEstimator, any_classifier, any_preprocessing
from hyperopt import tpe

# define dataset
X, y = make_classification(n_samples=100, n_features=10, n_informative=5, n_redundant=5, random_state=1)

# split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=1)

# define search
model = HyperoptEstimator(classifier=any_classifier("cla"), preprocessing=any_preprocessing("pre"), algo=tpe.suggest, max_evals=50, trial_timeout=30)

# perform the search
model.fit(X_train, y_train)

# summarize performance
accuracy = model.score(X_test, y_test)
print(f"Accuracy: {accuracy}")

# summarize the best model
print(model.best_model)

# the problem is that hyperopt sklearn is not advancing


# https://www.analyticsvidhya.com/blog/2020/09/alternative-hyperparameter-optimization-technique-you-need-to-know-hyperopt/
# alternatives for hyperopt

# other materials:
# https://www.ml4aad.org/wp-content/uploads/2018/09/chapter5-hyperopt-sklearn.pdf

# https://neptune.ai/blog/optuna-vs-hyperopt


# https://hyperopt.github.io/hyperopt-sklearn/


# https://machinelearningmastery.com/hyperopt-for-automated-machine-learning-with-scikit-learn/

# https://towardsdatascience.com/automl-in-python-a-comparison-between-hyperopt-sklearn-and-tpot-8c12aaf7e829


