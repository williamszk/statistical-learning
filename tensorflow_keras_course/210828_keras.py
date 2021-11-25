#%%
import pandas as pd
pd.set_option('display.max_columns', None)
import numpy as np
import seaborn as sns
sns.set()
import matplotlib.pyplot as plt

# %%
df = pd.read_csv("../data/kc_house_data.csv")

# number of missing
df.isnull().sum()

# 
df.describe().T

#%%
plt.figure(figsize=(10,6))
sns.histplot(df["price"])
#%%
sns.countplot(data=df, x="bedrooms")

sns.histplot(data=df, x="bathrooms")

#%%
df.corr()["price"].sort_values()
#%%
plt.figure(figsize=(10,6))
sns.scatterplot(x="price", y="sqft_living", data=df)
#%%
plt.figure(figsize=(10,6))
sns.scatterplot(x="price", y="bedrooms", data=df)
#%%
plt.figure(figsize=(10,6))
sns.boxplot(x="bedrooms", y="price", data=df)

#%%
plt.figure(figsize=(10,6))
sns.scatterplot(x="price", y="long", data=df)
#%%
plt.figure(figsize=(10,6))
sns.scatterplot(x="price", y="lat", data=df)

# %%
df.shape
#%%
plt.figure(figsize=(12,8))
sns.scatterplot(x="long", y="lat", data=df)

# %%
plt.figure(figsize=(12,8))
sns.scatterplot(x="long", y="lat", data=df, hue="price")
# %%
df_2 = df.copy()
df_2["price_sqm"] = df["price"]/df["sqft_living"]
quantile_cut = df_2["price_sqm"].quantile(.95)
mask = df_2["price_sqm"] < quantile_cut
df_2 = df_2[mask]

plt.figure(figsize=(12,8))
sns.scatterplot(x="long", y="lat", data=df_2, hue="price_sqm", 
                edgecolor=None, alpha=.2, palette='RdYlGn')
# %%
plt.figure(figsize=(10,6))
sns.histplot(data=df_2, x="price_sqm")
# %%
sns.boxplot(x="waterfront", y="price_sqm", data=df_2)

# %%

df.head()
df = df.drop("id", axis=1)
df["date"] = pd.to_datetime(df["date"])
df["date"]

df["year"] = df["date"].apply(lambda x: x.year)
df["month"] = df["date"].apply(lambda x: x.month)

df["price_sqm"] = df["price"]/df["sqft_living"]
#%%
df.head()

#%%
plt.figure(figsize=(12,8))
sns.boxplot(x="month", y="price_sqm", data=df)

# %%
df.groupby("month").mean()["price_sqm"].plot()
df.groupby("year").mean()["price_sqm"].plot()
df["year"].value_counts()

df = df.drop("date", axis=1)
df = df.drop("zipcode", axis=1)
# df = df.drop("yr_renovated", axis=1)

#%%
df.head()
# df["renovated"] = df["yr_renovated"].apply(lambda x: 1 if x>0 else 0)

df["sqft_basement"].value_counts()
# df["basement"] = df["sqft_basement"].apply(lambda x: 1 if x>0 else 0)

#%%

df = df.drop("price_sqm", axis=1)

#%%
X = df.drop("price", axis=1).values
y = df["price"].values

#%%
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.33, random_state=101)
# %%
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)

# %%
X_test = scaler.transform(X_test)

#%%

X_train.shape

#%%
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()
model.add(Dense(19, activation="relu"))
model.add(Dense(19, activation="relu"))
model.add(Dense(19, activation="relu"))
model.add(Dense(19, activation="relu"))
model.add(Dense(1))
model.compile(optimizer="adam", loss="mse")

model.fit(x=X_train, y=y_train, 
          validation_data=(X_test, y_test), 
          batch_size=128, epochs=400)

# %%
# save the model to be used later
from tensorflow.keras.models import load_model
model.save('../models/my_house_pricing_model_keras.hdf5')

# %%
# load the the saved model
later_model = load_model('../models/my_house_pricing_model_keras.hdf5')
# later_model.predict(new_gem)

# %%
losses = pd.DataFrame(model.history.history)
losses.plot()
# %%
from sklearn.metrics import mean_squared_error, mean_absolute_error, explained_variance_score

predictions = model.predict(X_test)

mean_squared_error(y_test, predictions)**.5

mean_absolute_error(y_test, predictions) 

np.mean(np.abs((y_test - predictions.reshape(-1,))/y_test))

explained_variance_score(y_test, predictions)



# %%
plt.figure(figsize=(10,8))
plt.scatter(y_test, predictions)
plt.plot(y_test, y_test, 'r')
# %%
single_house = df.drop("price", axis=1).iloc[0]
single_house = scaler.transform(single_house.values.reshape(-1,19))
model.predict(single_house)
df.iloc[0]