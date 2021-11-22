# https://www.udemy.com/course/complete-tensorflow-2-and-keras-deep-learning-bootcamp/learn/lecture/16904692#overview

#%%
from time import perf_counter
import pandas as pd
pd.set_option('display.max_columns', None)
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# %%
df_00 = pd.read_csv("../data/kc_house_data.csv")

df_00.isnull().sum()

df_00.describe().transpose()

df_00.head()

sns.displot(data=df_00, x="price")
sns.displot(data=df_00, x="bedrooms")

sns.countplot(data=df_00, x="bedrooms")

df_00.corr()["price"].sort_values()


df_00.corr()["price"].sort_values()

# zipcode         -0.053402
# id              -0.016772
# long             0.022036
# condition        0.036056
# yr_built         0.053953
# sqft_lot15       0.082845
# sqft_lot         0.089876
# yr_renovated     0.126424
# floors           0.256804
# waterfront       0.266398
# lat              0.306692
# bedrooms         0.308787
# sqft_basement    0.323799
# view             0.397370
# bathrooms        0.525906
# sqft_living15    0.585241
# sqft_above       0.605368
# grade            0.667951
# sqft_living      0.701917
# price            1.000000

#%%
# explore highly correlated features with the 
# target variable using scatter plot

sns.scatterplot(x="sqft_living", y="price", data=df_00)

# we can also use box plots to explore the relationship
# between two variables
# specially with a target variable and some feature
sns.boxplot(x="bathrooms", y="price", data=df_00)

# plot geographic information
sns.scatterplot(x="long", y="lat", data=df_00, hue="price")
#%%
df_00 = pd.read_csv("../data/kc_house_data.csv")
# drop outlier prices to make the map show a better color pallete
df_00.shape
p99_price_df_00 = np.percentile(df_00["price"], [99])[0]
mask = df_00["price"] < p99_price_df_00
df_00 = df_00[mask].copy()
df_00.shape

sns.scatterplot(x="long", y="lat", data=df_00, hue="price")

df_00["price_log"] = np.log(df_00["price"])

sns.scatterplot(x="long", y="lat", data=df_00, hue="price_log")

df_00["price_area_log"] = np.log(df_00["price"]/df_00["sqft_living"])
sns.scatterplot(x="long", y="lat", data=df_00, hue="price_area_log")

sns.scatterplot(x="long", y="lat", data=df_00, hue="price_area_log",
    edgecolor=None, alpha=0.2, palette="RdYlGn")

df_00.columns
sns.boxplot(x="waterfront", y="price", data=df_00)
sns.boxplot(x="waterfront", y="price_area_log", data=df_00)


#%%
# https://www.udemy.com/course/complete-tensorflow-2-and-keras-deep-learning-bootcamp/learn/lecture/16919900#overview
df_00 = pd.read_csv("../data/kc_house_data.csv")
df_00.head()
p99_price_df_00 = np.percentile(df_00["price"], [99])[0]
mask = df_00["price"] < p99_price_df_00
df_01 = df_00[mask].copy()

df_01["price_log"] = np.log(df_01["price"])
df_01["price_area_log"] = np.log(df_01["price"]/df_01["sqft_living"])

df_01 = df_01.drop("id", axis=1)
df_01["date"] = pd.to_datetime(df_01["date"])
df_01["year"] = df_01["date"].dt.year
df_01["month"] = df_01["date"].dt.month
df_01 = df_01.drop("date", axis=1)
df_01 = df_01.drop("zipcode", axis=1)
# df_01 = df_01.drop("yr_renovated", axis=1)
#%%
sns.boxplot(x="month", y="price_area_log", data=df_01)

sns.boxplot(x="year", y="price_area_log", data=df_01)

#%%

# for NN we need to scale our data
# because the optimization algorithm uses
# gradient descent
# will not scalling the features affect 
# prediction capabilities of the mode?

# https://www.udemy.com/course/complete-tensorflow-2-and-keras-deep-learning-bootcamp/learn/lecture/16904706#overview
df_01.columns
X_features = df_01.drop(["zipcode","price", "price_log", "price_area_log"], axis=1)
X_features.columns
# ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors',
#    'waterfront', 'view', 'condition', 'grade', 'sqft_above',
#    'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode', 'lat', 'long',
#    'sqft_living15', 'sqft_lot15', 'year', 'month']
X_features = X_features.values
y_target = df_01["price"].values
#%%
from sklearn.model_selection import train_test_split

X_features_train, X_features_test, y_target_train, y_target_test = train_test_split(
    X_features, y_target, test_size=0.3, random_state=101)

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
# scaler.data_max_
# scaler.data_min_

X_features_train_scaled = scaler.fit_transform(X_features_train)
scaler.data_max_
scaler.data_min_

X_features_test_scaled = scaler.transform(X_features_test)

#%%

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()

X_features_train_scaled.shape

model.add(Dense(19, activation="relu"))
model.add(Dense(19, activation="relu"))
model.add(Dense(19, activation="relu"))
model.add(Dense(19, activation="relu"))

model.add(Dense(1))

model.compile(optimizer="adam", loss="mse")

#%%
start = perf_counter()
model.fit(x=X_features_train_scaled, y=y_target_train, 
   validation_data=(X_features_test_scaled, y_target_test),
   batch_size=128, epochs=400
   )
elapsed_time = perf_counter() - start
print(f"elapsed_time = ")

model.save("../models/211121_01_keras_house_price.hdf5")

#%%

from tensorflow.keras.models import load_model

model_house_price = load_model("../models/211121_01_keras_house_price.hdf5")

# %%
loss_values = model.history.history.get("loss")
pd.Series(loss_values).plot()
#%%
loss_values = model.history.history
loss_values.keys()
df_loss_values = pd.DataFrame(loss_values)
df_loss_values.plot()
#%%
from sklearn.metrics import mean_absolute_error

#%%
start = perf_counter()
y_target_test_prediction = model_house_price.predict(X_features_test_scaled).reshape(-1,)
elapsed_time = perf_counter() - start
print(f"elapsed_time: {elapsed_time}")

#%%
a_house_observation = [list(X_features_test_scaled[0])]
start = perf_counter()
float(model_house_price.predict(a_house_observation)[0])
elapsed_time = perf_counter() - start
print(f"elapsed_time: {elapsed_time}")
#%%
print("On train dataset:")
y_target_train_prediction = model_house_price.predict(X_features_train_scaled).reshape(-1,)
mae_price_house = mean_absolute_error(y_target_train, y_target_train_prediction)
print(f"{mae_price_house = }")
mean_y_target_train = y_target_train.mean()
print(f"{mean_y_target_train = }")
percent_error_target_price = mae_price_house/mean_y_target_train
print(f"{percent_error_target_price = }")
#%%
print("On test dataset:")
mae_price_house = mean_absolute_error(y_target_test, y_target_test_prediction)
print(f"{mae_price_house = }")
mean_y_target_test = y_target_test.mean()
print(f"{mean_y_target_test = }")
percent_error_target_price = mae_price_house/mean_y_target_test
print(f"{percent_error_target_price = }")
# %%
# https://www.udemy.com/course/complete-tensorflow-2-and-keras-deep-learning-bootcamp/learn/lecture/16904710#overview

from sklearn.metrics import explained_variance_score
explained_variance_score(y_target_test, y_target_test_prediction)
explained_variance_score(y_target_train, y_target_train_prediction)
#%%
sns.scatterplot(x=y_target_test, y=y_target_test_prediction)
plt.plot(y_target_test, y_target_test, "r")
# %%





