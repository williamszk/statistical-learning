# https://www.udemy.com/course/complete-tensorflow-2-and-keras-deep-learning-bootcamp/learn/lecture/17029924#overview
#%%
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from tensorflow.keras.datasets import mnist

#%%
(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train.shape
y_train.shape
X_test.shape
y_test.shape

#%%
single_image = X_train[0]
single_image.shape
plt.imshow(single_image)
y_train[0]
#%%
single_image = X_train[1]
plt.imshow(single_image)
y_train[1]
#%%
from tensorflow.keras.utils import to_categorical

y_train_onehot = to_categorical(y_train)
y_train_onehot.shape
y_train_onehot[0]
y_train_onehot[1]
#%%
# For the scalling we can just divide by 255.
# In this particular case, because all images should have values between 0 and 255.
X_train_scaled = X_train/255
X_test_scaled = X_test/255
# So in this particular case we don't need to worry importing a scaler
# do the .fit on the training data and then do the .fit on both the 
# training and test datasets. We can just pass a division of 255.
# Of course here we are using assuming a scaler like a MinMaxScaler.
# We want to make all values between 0 and 1.

#%%
# take a look at the image of a scaled X
plt.imshow(X_train_scaled[0])
X_train_scaled[0]

#%%
# The CNN will expect a dimension for the RGB channel.
# So the shape that is expected is (60000, 28, 28, 3)
# notice the 3 at the end.
# But we need to explicitly tell the Convolutional Neural Network
# that we want to use just one channel.
X_train_scaled.shape
X_train_scaled_1channel = X_train_scaled.reshape(60000, 28, 28, 1)
X_train_scaled_1channel.shape
# (60000, 28, 28, 1)
# batch_size = 60000
# width = 28
# height = 28
# n_color_channel = 1

#%%
# Do the same reshaping for the test dataset
X_test_scaled.shape
X_test_scaled_1channel = X_test_scaled.reshape(10_000, 28, 28, 1)
X_test_scaled_1channel.shape

#%%




#%%






