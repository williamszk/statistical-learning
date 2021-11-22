#%%
# https://www.udemy.com/course/complete-tensorflow-2-and-keras-deep-learning-bootcamp/learn/lecture/16844530#overview

import pandas as pd
import numpy as np
import seaborn as sns
sns.set()

# %%
df_00 = pd.read_csv("../data/fake_reg.csv")
df_00
#%%
# supervised learning problem
sns.pairplot(df_00)


# %%


# tensor flow only accepts only numpy arrays
# we need to separate the featues and from the target variable

X_features = df_00.loc[:, ["feature1", "feature2"]].values
y_target = df_00["price"].values
#%%
from sklearn.model_selection import train_test_split

list_result_train_test = train_test_split(
    X_features, 
    y_target,
    test_size=0.3,
    random_state=42
)

X_features_train = list_result_train_test[0]
X_features_test = list_result_train_test[1]
y_target_train = list_result_train_test[2]
y_target_test  = list_result_train_test[3]

X_features_train.shape
X_features_test.shape
#%%
# weights and biases
# we need to normalize the training data
# also we need to normalize the incoming data
# for the prediction
# this another step that needs to be made in the case
# of neural networks

from sklearn.preprocessing import MinMaxScaler
help(MinMaxScaler)
# MinMax scaler set values between 0 and 1
# 
scaler_minmax = MinMaxScaler()
scaler_minmax.fit(X_features_train)
# we don't want to use the test set also
# in the minmax scaler, to prevent data likeage
# we should treat the test set as totally unknown

X_features_train_scaled = scaler_minmax.transform(X_features_train)
X_features_test_scaled = scaler_minmax.transform(X_features_test)

# %%
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# help(Sequential)
# help(Dense)
#%%

# this one way of creating the model
model = Sequential([
    Dense(4,activation="relu"),
    Dense(2,activation="relu"),
    Dense(1)
])

#%%
model = Sequential()

model.add(Dense(4, activation="relu"))
model.add(Dense(2, activation="relu"))
model.add(Dense(1))

# %%

model = Sequential()
model.add(Dense(4, activation="relu"))
model.add(Dense(4, activation="relu"))
model.add(Dense(4, activation="relu"))
model.add(Dense(1))

model.compile(optimizer="rmsprop", loss="mse")
# %%
model.fit(
    x=X_features_train_scaled,
    y=y_target_train,
    epochs=250
)
# %%
loss_values = model.history.history.get("loss")
pd.Series(loss_values[110:]).plot()
# %%
model.evaluate(
    x=X_features_train_scaled,
    y=y_target_train)
# 23.91565
#%%
model.evaluate(
    x=X_features_test_scaled,
    y=y_target_test)
# 25.71476173400879
# %%
y_target_prediction = model.predict(x=X_features_test_scaled).reshape(-1,)
y_target_test

# y_target_prediction.shape
# y_target_test.shape

df_prediction = pd.DataFrame(
    {"y_target_prediction": y_target_prediction,
    "y_target_test": y_target_test
    })

df_prediction.plot()

sns.relplot(
    x="y_target_test", 
    y="y_target_prediction",
    data=df_prediction)

# %%
from sklearn.metrics import mean_absolute_error, mean_squared_error

mean_absolute_error(y_target_test, y_target_prediction)
mean_squared_error(y_target_test, y_target_prediction)

#%%
# for a new point entering the model
new_gem = [[998,1000]]
new_gem_scaled = scaler_minmax.transform(new_gem)
target_prediction = model.predict(new_gem_scaled)[0][0]

target_prediction
# 420.25565
# %%
# save the model to persistent memory
from tensorflow.keras.models import load_model
model.save("../models/my_gem_model_211120.hdf5")
#%%
# load the model
model_gem_price = load_model("../models/my_gem_model_211120.hdf5")
model_gem_price

model_gem_price.predict(new_gem_scaled)