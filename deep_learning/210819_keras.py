import pandas as pd
import numpy as np
import seaborn as sns
from tensorflow.python.ops.gen_array_ops import pad_eager_fallback
sns.set()



df = pd.read_csv("../data/fake_reg.csv")

sns.pairplot(df)


from sklearn.model_selection import train_test_split

X = df[["feature1", "feature2"]].values
y = df["price"].values

X_train, X_test, y_train, y_test = \
    train_test_split(
        X, y, test_size=0.3, 
        random_state=42)

# train_test_split?

X_train.shape
X_test.shape


from sklearn.preprocessing import MinMaxScaler
# help(MinMaxScaler)

scaler = MinMaxScaler()
scaler.fit(X_train)
# data leakege
# 
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

X_train.max()
X_train.min()

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# read the documentation of Sequential and Dense
#%%
model = Sequential([
    Dense(4, activation="relu"), 
    Dense(2, activation="relu"),
    Dense(1)
    ])

# a Dense Layer is a layer that is connected
# to all nodes 
#%%
# below is another way to build the model
model = Sequential()
model.add(Dense(4, activation="relu"))
model.add(Dense(2, activation="relu"))
model.add(Dense(1))


#%%
model = Sequential()
model.add(Dense(4, activation="relu"))
model.add(Dense(4, activation="relu"))
model.add(Dense(4, activation="relu"))
model.add(Dense(1))

model.compile(optimizer="rmsprop",
              loss="mse")

#%%
model.fit(x=X_train, y=y_train, epochs=250)
#%%
df_loss = pd.DataFrame(model.history.history)
df_loss.plot()


#%%
# the last layer will determine what type of
# model will be produced
# in a regression problema we leave the 
# last layer with a identity activation function
# if the problema was a classifcation problem
# we shoul use more final neurons and with 
# a different activation function like
# a sigmoid

# what are the parameters for the "compile()" method?
# multi-class classification problem
model.compile(optimizer="rmsprop",
              loss="categorical_crossentropy",
              metrics=["accuracy"])

# for binary classification problem
model.compile(optimizer="rmsprop",
              loss="binary_crossentropy",
              metrics=["accuracy"])

# for a regression problem
model.compile(optimizer="rmsprop",
              loss="mse")

#%%


# some notes
"""
In the world of neural networks
and linear regression specially for machine learning
it is a good practive to scale the variables
there are some options: standar scaler, minmax scaler
this is important for models that use gradient descent
optimazition.
If the features are not scalled the hyper surface of
features and loss function will be distorted.
And it may cause difficulty for the optimization 
algorithm to find the optimum point. 

For tree methods this is not a problem. 
Decision trees do not use gradient descent as 
optimization algorithms.

For inference models (am I using the word 'inferece' 
in the right context here?) the scalaing of the variables
may be not what we want to do. 
I did not see in econometrics books scalling is not
mentioned. (find out books to read about) 
That is because for inference we want to find how 
explatory variables are affecting the explained variable
(target variable). Usually this is done in linear regression.

"""

"""
Another discussion: 
The word inference. 
Inferential statistics.
I think that inference does not mean causal.
For example inferential can refer to something
like using a sample to know how the population
behaves.

Usually there is a distinction between inferential
models and predictive models.

"""

"""
Make a discussion about the words
"Decision Trees"
"Regression Trees"
"Classification Trees"
What are the differences between those words?

"""


#%%

y_test
X_test

model.evaluate(X_train, y_train, verbose=0)
model.evaluate(X_test, y_test, verbose=0)

#%%

test_predictions = model.predict(X_test)
test_predictions = pd.Series(test_predictions.reshape(-1,)) 
y_test_series = pd.Series(y_test)
df_pred = pd.concat([y_test_series, test_predictions], axis=1)
df_pred.columns = ["observed","predicted"]

sns.pairplot(df_pred)
sns.scatterplot(data=df_pred, x="observed", y="predicted")
#%%

from sklearn.metrics import mean_absolute_error, mean_squared_error

mean_absolute_error(df_pred["observed"], df_pred["predicted"])

mean_squared_error(df_pred["observed"], df_pred["predicted"])**.5

df.describe()

#%%
new_gem = [[998,1000]]
new_gem = scaler.transform(new_gem)
model.predict(new_gem)
#%%

from tensorflow.keras.models import load_model
model.save('../models/my_gem_model.hdf5')

#%%

later_model = load_model('../models/my_gem_model.hdf5')
later_model.predict(new_gem)