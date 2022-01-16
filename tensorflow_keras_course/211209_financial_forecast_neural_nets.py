#%%
import pandas as pd
import pandas_datareader as pdr
import seaborn as sns
sns.set()

# https://www.alpharithms.com/python-financial-data-491110/
# use Nvidia financial data for forcasting
df_00 = pdr.get_data_yahoo("NVDA")

# we could also use high-frequency data to make forecasting
df_00

# reset index, make date a field of the table
df_00 = df_00.reset_index()

#%%
# we'll try to predict the Open value of the time series
# first we'll try to use a simple linear regression with 1 to 5 lags
# in time
# then we'll try the same with neural network, 1 to 5 lags
# but we'll include 2 layers of 20 vertices each
# let's see what happens
# we'll use keras
df_00

# I've seem that for time series and any type of data that 
# have a sequence, people suggest using RNN, but can't we
# build a time series model with just an usual ANN?
# That is what we'll try here.

# Stock market price prediction is hard.
# It is more feasible to predict volatility but the value prediction
# is by the nature of the problem a hard task.

#%%
# Use only variables: ["Date", "Open"] for the analysis
df_01 = df_00.loc[:,["Date", "Open"]].copy()
df_01

sns.lineplot(x="Date", y="Open", data=df_01)

# for the train test split we'll use "Date" as the variable

# Obs: RNN are not DAGs, they have cycles in their dependency graphs...
# So we can say that an RNN is not a feed-forward network.
# A MLP (Multi Layer Perceptron) is a feed-forward network.

# Usually in an ANN all hidden layers have the same activation function
# but the output layer will have a different activation function
# it depends on the type of the problem:
# if we have a classification problem: we'll use a sigmoid or hyperbolic tangent function
# if we have a regression problem: we'll use the identity function

# Do we use back-propagation in RNNs?





























