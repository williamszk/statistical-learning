# ---------------------------------------- #
# study notes:
# chapter 10 of aurelian geron's book
# ---------------------------------------- #

# TLU = Threshold Logic Unit

import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import Perceptron

df_iris = load_iris()

type(df_iris)

dir(df_iris)
# ['DESCR',
#  'data',
#  'data_module',
#  'feature_names',
#  'filename',
#  'frame',
#  'target',
#  'target_names']

print(df_iris.DESCR)

# What is inside df_iris.data?
df_iris.data
# this sia matrix of numpy array

# what is inside df_iris.target?
df_iris.target
# numpy array with 3 values, for the different types of iris species

# why only take features 2 and 3? Those are only petal length and petal width
X_features = df_iris.data[:,[2,3]]
y_target = (df_iris.target == 0).astype(int)

type(y_target[0])
# numpy.int32

# create the instance of class Perceptron
perceptron_classifier = Perceptron()

# in the documention of Perceptron:
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html
# """
# The Perceptron is another simple classification algorithm suitable for large scale learning. 
# By default:
# It does not require a learning rate.
# It is not regularized (penalized).
# It updates its model only on mistakes.
# The last characteristic implies that the Perceptron is slightly faster to 
# train than SGD with the hinge loss and that the resulting models are sparser.
# """

type(perceptron_classifier)
# sklearn.linear_model._perceptron.Perceptron

# without any train_test split we can just fit the model
perceptron_classifier.fit(X_features, y_target)

y_prediction = perceptron_classifier.predict([[2, 0.5]])
# >>> y_prediction
# array([0])

y_prediction = perceptron_classifier.predict([[0, 0.5]])
# y_prediction
# array([1])

# From the book:
# You may have noticed that the Perceptron learning algorithm strongly resembles Sto‐
# chastic Gradient Descent. In fact, Scikit-Learn’s Perceptron class is equivalent to
# using an SGDClassifier with the following hyperparameters: loss="perceptron",
# learning_rate="constant", eta0=1 (the learning rate), and penalty=None (no
# regularization).

# ------------------------------------------------ #

# the passthrough input layer
# passthrough means that the numbers are passed as they are

# FNN = feed forward neural network
# DNN = Deep Neural Networks
# Backpropagation = gradient descent with some differences
# for backpropagation the methods use automatic differentiation
# autodiffs
# autodiffs have many forms
# backpropagations uses "reverse-mode autodiff"
# 

# mini-batch e.g. 32 observations at a time
# the training goes throught the whole dataset many times
# each time that the models uses the whole datset is called an epoch
#
# in the "forward pass" we calculate all values that are the combinations
# of the inputs and the intermediary output values and the otuput of the 
# network.
# 
# Then the algorithms calcualtes the total error of the network
# here we can use a loss function
#
# Then the algorithm calculates by how much each layer connection
# contributed to the final error.
# It uses the chain rule, an analytical version of the chain rule.
#
# Then the algorithm changes the weights of each connection
# to decrease the error, it uses gradient descent for this
#
#


# other popular activation functions
# hyperbolic tangent
# rectified linear unit (relu)
# 

# How backpropagation works exactly?










