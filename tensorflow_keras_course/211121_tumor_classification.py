# https://www.udemy.com/course/complete-tensorflow-2-and-keras-deep-learning-bootcamp/learn/lecture/16919956#overview
#%%
import json

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.python.keras import callbacks
sns.set()
# %%
df_00 = pd.read_csv("../data/cancer_classification.csv")

#%%
df_00.info()

df_00.describe().transpose()

#%%
sns.countplot(x="benign_0__mal_1", data=df_00)

df_00.corr()["benign_0__mal_1"].sort_values().drop("benign_0__mal_1").plot(kind="bar")

sns.heatmap(df_00.corr())

#%%
X_features = df_00.drop("benign_0__mal_1", axis=1).values
y_target = df_00["benign_0__mal_1"].values

len(y_target)
X_features.shape
#%%
from sklearn.model_selection import train_test_split
X_features_train, X_features_test, y_target_train, y_target_test = \
    train_test_split(X_features, y_target, test_size=0.25, random_state=101)

X_features_train.shape
X_features_test.shape
# %%
from sklearn.preprocessing import MinMaxScaler

scaler_minmax = MinMaxScaler()
X_features_train_scaled = scaler_minmax.fit_transform(X_features_train)
X_features_test_scaled = scaler_minmax.transform(X_features_test)
# %%
# https://www.udemy.com/course/complete-tensorflow-2-and-keras-deep-learning-bootcamp/learn/lecture/16919964#overview

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()

model.add(Dense(30, activation="relu"))
model.add(Dense(15, activation="relu"))
# Binary Classification
model.add(Dense(1, activation="sigmoid"))

model.compile(loss="binary_crossentropy", optimizer="adam")

# %%
model.fit(
    x=X_features_train_scaled, 
    y=y_target_train,
    epochs=600,
    validation_data=(X_features_test_scaled, y_target_test)
    )

# save model 
model.save("../models/tumor_prediction_211121.hdf5")
# save history of model as pickle
model_history = model.history.history

with open("../models/model_history_tumor_211121.json", "w") as file:
    json.dump(model_history, file, indent=4)

# %%
with open("../models/model_history_tumor_211121.json", "r") as file:
    model_history_2 = json.load(file)

#%%
pd.DataFrame(model_history).plot()
pd.DataFrame(model_history_2).plot()
# examples of overfitting
#%%
from tensorflow.keras.models import load_model
model_tumor = load_model("../models/tumor_prediction_211121.hdf5")

#%%
# use early stopping

model_early_stop = Sequential()

model_early_stop.add(Dense(30, activation="relu"))
model_early_stop.add(Dense(15, activation="relu"))
# Binary Classification
model_early_stop.add(Dense(1, activation="sigmoid"))

model_early_stop.compile(loss="binary_crossentropy", optimizer="adam")

# %%
from tensorflow.keras.callbacks import EarlyStopping

early_stop = EarlyStopping(monitor="val_loss", mode="min", verbose=1, patience=25)

model_early_stop.fit(
    x=X_features_train_scaled, 
    y=y_target_train,
    epochs=600,
    validation_data=(X_features_test_scaled, y_target_test),
    callbacks=[early_stop]
    )

# save model 
model_early_stop.save("../models/tumor_prediction_211121_early_stop.hdf5")
# save history of model as pickle
model_history_early_stop = model_early_stop.history.history

with open("../models/model_history_tumor_211121_early_stop.json", "w") as file:
    json.dump(model_history_early_stop, file, indent=4)

# %%
with open("../models/model_history_tumor_211121_early_stop.json", "r") as file:
    model_history_early_stop_2 = json.load(file)

pd.DataFrame(model_history_early_stop_2).plot()
#%%

from tensorflow.keras.layers import Dropout

# drop out layers
model_drop_out = Sequential()

model_drop_out.add(Dense(30, activation="relu"))
model_drop_out.add(Dropout(0.5))

model_drop_out.add(Dense(15, activation="relu"))
model_drop_out.add(Dropout(0.5))

# Binary Classification
model_drop_out.add(Dense(1, activation="sigmoid"))

model_drop_out.compile(loss="binary_crossentropy", optimizer="adam")

early_stop = EarlyStopping(monitor="val_loss", mode="min", verbose=1, patience=25)

model_drop_out.fit(
    x=X_features_train_scaled, 
    y=y_target_train,
    epochs=600,
    validation_data=(X_features_test_scaled, y_target_test),
    callbacks=[early_stop]
    )

# save model 
model_drop_out.save("../models/tumor_prediction_211121_drop_out.hdf5")
# save history of model as pickle
model_history_drop_out = model_drop_out.history.history

with open("../models/model_history_tumor_211121_drop_out.json", "w") as file:
    json.dump(model_history_drop_out, file, indent=4)
# %%
# %%
with open("../models/model_history_tumor_211121_drop_out.json", "r") as file:
    model_history_drop_out_2 = json.load(file)

pd.DataFrame(model_history_drop_out_2).plot()
# %%
model_drop_out_2 = load_model("../models/tumor_prediction_211121_drop_out.hdf5")

from sklearn.metrics import classification_report, confusion_matrix

# I need a threshold 
y_target_predicted = (model_drop_out_2.predict(X_features_test_scaled) > 0.5).astype(int)
type(y_target_predicted[0][0])

print(classification_report(y_target_test, y_target_predicted))
print(confusion_matrix(y_target_test, y_target_predicted, labels=[0,1]))

