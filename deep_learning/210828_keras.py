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

