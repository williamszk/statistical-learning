#!/usr/bin/env python
# coding: utf-8

# # Loan Prediction
# 
# Author: William Suzuki
# 
# Date: Novemeber 2021
# 

# This is an attempt to build a model to predict if a person is going to pay the loan or not.
# 
# There are many insights and comments in this notebook, that can be used for later usage and other projects.

# In[1]:


import sys
from datetime import datetime
from importlib import reload
import pandas as pd
pd.set_option('display.max_columns', None)
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

sys.path.append(".")
import helper_script as hs

reload(hs)


# In[3]:
# the dataset with metadata about the dataset
df_metadata = pd.read_csv("../data/lending_club_info.csv", index_col="LoanStatNew")
df_00 = pd.read_csv("../data/lending_club_loan_two.csv")
df_00

# In[4]:
# which is the target variable?
target_variable = "loan_status"
# this is one of the most important things to determine
# when we are working with a supervised learning problem

# In this dataset we have a variable that tells when the loan was issued: `issue_d`.  
# To simulate a scenario of new loans coming we should split according to time. 
# We do this we do this with the intent to simulate a deployment scenario.

# In[5]:
df_00["issue_d"]

# In[6]:
# it is string
df_00["issue_d"].dtype 

# In[7]:
df_00["issue_d"].hist()

# Is this division going to affect the performance  of model in the end (real deploy)?
# 
# Yes it will.
# 
# But if we want to know how the data drifts and how the model will perform in this circunstances we should split according to time.
# 
# I should research more about this...
# 
# 
# The best think to do in the end is to use all the data that we have available to train the model.
# In[8]:
# How to convert string into year-month?
issue_date = pd.to_datetime(df_00["issue_d"], exact=False)

# Remeber that this step is used just for the train test split  according to year-month of loan issue. 
# So we shouldn't include the `issue_data` variable into the data frame.
# In[9]:
issue_date.hist(bins=60)

# In[10]:
issue_date.value_counts().sort_index()
# In[11]:
# find where the median of the distribution of dates is:
list(issue_date.sort_values())[len(issue_date)//2]

# In[12]:
# Find where 70% percentile of the distribution is:
list(issue_date.sort_values())[int(len(issue_date)*0.7)]
# Obs: using np.quantile doesn't work with timestamp datatype.

# Without the `list()` around the `pd.Series` the index will take the pd.Series' index.
# 
# We'll make `2015-01` as the threshold for training and test.
# In[14]:
threshold_date_train_test_split = datetime(2015,1,1)
mask_train = issue_date <= threshold_date_train_test_split

# verify if the proportion for train data makes sense
mask_train.sum()/len(mask_train)

# In[15]:
# Make the train_test_split using the time variable
df_features_train = df_00[mask_train].drop(target_variable, axis=1)
df_features_test = df_00[~mask_train].drop(target_variable, axis=1)
df_target_train = df_00[mask_train][target_variable]
df_target_test = df_00[~mask_train][target_variable]

#%%
# Below is the previous attempt to make a train and test split.
# 
# This is an important issue, when you have a new dataset and you are worried about the production phase. 
# 
# We should see if there are any variable that tell us when the data arrived, this variable can be used to make the train test split. 
# 
# What are the drawbacks of this strategy?
# 
# The alternative option is to just split using the `train_test_split()` from `sklearn` function, without considering
# the date when the data arrived.
# 
# What are the advantages and disadvantages of doing the train test split with a time variable?
# 
# I think that in the end we should be using the whole dataset to train the model.
# 
# But for the understanding of the phenomena we should make a simulation of how the data is coming into the deployment setting.
# 
# This can help us undersatand model drift, and also think about continous learning of the model.
# 
# If we build our program around this form of spliting we can forsee challenges with continous training.
# 
# For example, we can see how the model adapts to the change of the data generating process.

# In[ ]:

# from sklearn.model_selection import train_test_split
# df_features_train, df_features_test, df_target_train, df_target_test = \
#     train_test_split(df_features, df_target, test_size=0.30, random_state=42)


# In[16]:
# this dataset will be used for exploratory data analysis
# feature engineering, and the creation of the feature pipeline
# and model training
df_features_train.shape


# In[17]:

# this will be used in a simulation like of deployment of the model
df_features_test.shape


# In[18]:


# this data will be used to train the model
# and determine the feature engineering steps that we'll need to make
df_target_train.shape


# In[19]:


# this data frame will only be used in the last of last steps
# when we want a final metric for model comparison
df_target_test.shape 


# What is more important?
# The production ready of the model?
# Or the most performatic model?
# We should first try to build a pipeline, production ready code with focus on 
# deployment.
# In most scenarios this is the priority order.
# But for research of the most performatic model is more relevant, and 
# this priority level can be more flexible.
# Even in more flexible situations we should focus on trying  to give 
# importance on how to serve the model.

# After building a production ready code we can  dedicate time for exploring the most performatic model.
# And new data will come and we'll need to observe the model drift and adapt the model for new scenarios.

# In[20]:
# join the features and the target variable again
df_train = pd.concat([df_features_train, df_target_train], axis=1)
df_train.head()

# For the EDA and the building of the feature engineering programs we should use the whole dataset as it is, with target 
# and features together in a single data frame.
# In the deployment simulation construction we can imagine that the data is 
# coming as dictionaries/json, this is not a  strong assumption. 
# Most probably the data will arrive in this format, but this depends on 
# the backend of the firm and how the get request responds.

# On the real deployment, we use absolutely all data that we have.
# But for studying and understanding the phonemenon we should make 
# the separation of data into training and test, and we should do 
# this in a most similar way to the deployment scenario as possible.

# What are the types of features that we have?
# Or even that exist?
# 1. We have numeric, which have an order.
# 2. We have categorical with some natural order.
# 3. And we have categorical without an order.
# 
# Are there any time/space features?
# Are there other types of information that can be 
# considered like time and space?

# In[21]:
# loan_amnt: amount applied by the borrower
df_train["loan_amnt"].hist(bins=60)
# In[22]:
# term, the amount of payments to be made in months
df_train["term"].hist()
# In[23]:
# int_rate: interest rates of the loan
df_train["int_rate"].hist(bins=60)
# In[24]:
# installment: the monthly value of the loan
df_train["installment"].hist(bins=60)

# Strategy for rapid iteration and value generation of the modelling effort:
# We try to run the model with just a subset of the features.
# This is clearly sub-optimal for model performance, but it is better
# for model delivery.
# We first see the most correlated variables with the target_variable.
# And use them as features. In this way we can have a benchmark later. 
# We can keep track of the progress of the model.
# Without benchmarks it is hard to measure the progress of a project.
# We can measure the progress of a project by the time that 
# we can deliver the code to the client, and by the precision of the model.
# There are other ways too... But I can think of the two above.

# In[26]:
# We need to transform the target_variable into a numeric variable
df_train[target_variable].hist()
# In[28]:
# The variable below will be used for model training.
loan_status_numeric = np.array([
    hs.convert_loan_status_into_numeric(x) for x in df_train[target_variable]])

loan_status_numeric
# All the functions that make some transformation of the data should take 
# individual values instead of for example using function that transform 
# the whole data frame. 
# That is, functions that have as arguments `pd.DataFrame` and the output 
# `pd.DataFrames`, shouldn't be used/created.
# What we should do is to build functions that have arguments that are of 
# primitive datatypes (int, str, float), and as outputs also primitive datatypes.

# For the test dataset we should simulate as if it was coming from the outside world. 
# So we should separate the training from test dataset since the beginning of our 
# analysis. 
# That is, before starting anything, this will make the analysis and 
# the challenge more difficult but it will simulate a situation of deployment.
# By the time that we use the test dataset, we'll need to think 
# how to preprocess the incoming data, so that it can be consumed 
# the `.predict` of the trained model.

# In[29]:
# grade: loan grade
df_train["grade"].hist(bins=30)
# I imagine that A is better than B, and so on...
# We can test this later.
# On this first stage we'll make univariate analysis of the variables.
# In[31]:
# sub_grade: 
plt.figure(figsize=(14, 6))
df_train["sub_grade"].hist(bins=70)
# In[33]:
# emp_title: the job title that the borrower told when applying for the loan
plt.figure(figsize=(12, 6))
df_train["emp_title"].value_counts()
#%%
# We have 143_694 different employee titles.
# This number is too high.
# This is a situation where we have too many different types 
# of categorical non-ordered possible values for a feature.
# I worked with this type of data in the insurance industry. 
# (I should revisit the code that I used there to see the methods 
# that I wrote to automatically group the categories that are too sparce)
# 
# We can also find a feature with too many categories 
# and that have some kind of ordering.
# If we're going to use this feature, first we'll need 
# to make some kind of grouping. 
# 
# For this we could use PCA or other type of 
# unsupervised learning method (I have to think more about this).
# 
# Another method that we could use is by ordering the features 
# according to how  the mean (or other measure, like median) in relation to the 
# target variable changes. 

# `emp_title` is an example of a categorical variable that does not have an order.
# I can think of two options when using this type of features:
# 1. Transform into integer; or 
# 2. Do one-hot enconding.

# But we also need to remember that the data that we see here are 
# for problems that are for tabular data. 
# I say "tabular data" in a way to differentiate for example to problems 
# like: image classification, NLP, and reiforcement learning.
# The methods of ANN can be used for tabular data problems. 
# So deep learning can be used for tabular data problems.
# Inside tabular data problems we can have supervised 
# (regression, classification) problems, and also unsupervised problems. 
# Maybe there is another name, a better name instead of tabular data problems. 
# I use this term in a sense to differentiate these types of 
# problems from the other machine learning problems: 
# NLP, image and sound processing, and RL.

# Thinking about the steps that we need to take when making EDA and 
# feature engineering.
# I think that mostly this is an art form. 
# In the sense that there is not set of steps that are perfect for 
# EDA or even for feature engineering. Nothing that I saw at least. 
# But this art is interesting to study and apply.

# I notice that the first thing that we need to do in a new dataset 
# is to go through each variable that we have and understand its meaning, 
# its meaning in the sense of the business or the domain problem.
# This step doesn't need to be too detailed, but have some depth
# to be effective in the modeling work.

# In this type of inquiry, we need to answer questions like:
# How this data is generated, and how is this applied to our problem?
# Make a histogram of the variable.
# Make a table of frequency of the variable.
# Verify if the variables is numeric or string. 
# If the variable is categorical, is categorical with some natural order? 
# Or it doesn't have an order?
# If the variable is categorical and with order, does the distance 
# between each category have some intrinsic meaning? If it does than maybe 
# this is a numeric discrete variable.
# If the variable is numeric the distance between the values have some meaning? 
# If it does (there is a name for this, I don't remember, it is related to ratio)
# If the variable is categorical but the distance doesn't have meaning, 
# this variable can be just a categorical with ordering.
# The variable can be a number but there is no order in them, 
# for example zip code.
# ....

# In[ ]:
# emp_length: duration in years of the employment of borrower
df_train["emp_length"].value_counts()
# This is a categorical values with a natural ordering
# We could use this variable for modeling
# but we'd need to tranform it into numeric first.

# Another important thing in feature engineering
# are problems where we need to save the modeling function
# the function have some kind of .fit step
# In the case of the function that transforms 
# e.g. < 1 year => 0 and 1 year => we can just build a function
# sklearn have a function that can concatenate this preprocessing
# step.

# https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html
# Search more about sklearn pipeline, and do some tutorials
#%%
plt.figure(figsize=(14, 6))
df_train["emp_length"].hist(bins=23)
# the legend is out of order

# In[ ]:
# home_ownership: 
df_train["home_ownership"].value_counts()
df_train["home_ownership"].hist()
# Comments:
# OTHER and NONE are too few to be able to use for modeling...
# We should group those categories into other categories.
# 
# When building the functions to group, we need to remember the values 
# that are used for grouping. Should we save them as dictionaries
# to be then saved as .pickle with the pipeline function?
# 
# Potentially we could have many of those preprocessing functions
# that need to have a .fit step.
# We should build those preprocessing functions in a sklearn
# API style. That is, with a .fit and a .transform method.
#
# One of the things that I imagine that the pipeline function will
# bring is the simplicity to save the functions into a single
# binary that can be easily imported and used.
#
# We can think that the preprocessing (which comprises the feature)
# engineering, and the .predict step of the model itself 
# can all be bundled into a single "function".
# This function would receive a dictionary/json object.
# And by itself it is able to process everything that is necessary
# and give a value which is the response. It should be a scalar 
# or a string (the category) or it should be another thing
# like a dictionary of probabilities.
#
# How `home_ownership` can affect the probability of a borrower to
# pay the loan?
# MORTGAGE    142846
# RENT        117531
# OWN          24863
# OTHER          112
# NONE            31
# 
# Comments:
# OTHER and NONE are too few to be able to use for modeling...
# We should group those categories into other categories.
#
# Maybe OWN has a less chance to not pay the loan
# compared to MORTGAGE and RENT
# In[ ]:
df_train["annual_inc"].hist(bins=60)
# there are some outliers for this variable
np.log(df_train["annual_inc"]).hist(bins=60)

df_train["annual_inc"].describe()
# count    2.853830e+05
# mean     7.271518e+04
# std      5.829517e+04
# min      4.000000e+03
# 25%      4.500000e+04
# 50%      6.200000e+04
# 75%      8.760000e+04
# max      8.706582e+06

# The highest income is 8,000,000 and the median is 620,000
# There are outliers for the annual income
# Should we drop observations for a feature that have outliers?
# I think this will not affect the performance of the model.
# We could make an empirical test.
# But we also could search more about this.
# It is clear to me that droping observations from the 
# target variable makes sense. Because this can affect the performance
# of the model for the most common values. (Do a test about this)
# But for to drop outliers from an explanatory features, this is not
# so clear to me.
# 
# https://towardsdatascience.com/ways-to-detect-and-remove-the-outliers-404d16608dba
# 

# I think that we shouldn't drop an observation that is an outliers
# on a explanatory feature. 
# Because on the deployment phase, we can't just drop a request because 
# one of the features is an outlier.
# It makes sense that on the training phase, we drop observations that
# are outliers on the target variable, because this can negatively
# affect our model performance.
# And we can say that for a certain range of values our model has poor 
# predicition performance.

# Another interesting idea is to understand how our model performs
# depending on different features. For example, we have a feature of
# annual_inc, plot a graph with annual_inc on the x-axis
# and model performance on the y-axis, then see how the 
# scatterplot behaves. We can make a moving window in graph too.
# The x-axis can have the time variable.
# Or if we are dealing with space, we can have a map
# to show which regions have poor performance or higher peformance.
# We need to be careful to be able to answer if the difference
# is statistically significant.

# https://www.theanalysisfactor.com/outliers-to-drop-or-not-to-drop/
# 
# This article have some interesting ideas about droping or not outliers.
#
# Dropping the outlier may depend on the type of model that we are using
# If the model is a linear regression, this is more compeling.
# But what if the model is a random forest? Or an ANN?

# In[ ]:
df_train["verification_status"].value_counts()
# verification_status: is the status if the income source was verified
# This is a categorical non-ordered feature.
# What is the expected relationship with the target variable?
#
# Verified           105073
# Not Verified        95077
# Source Verified     85233
#
# I expect that Verified and Source Verified are better than
# Not Verified
# 
# See if there is a relationship betwee annual_inc and verification_status
# Maybe higher annual_inc have less verification_status

sns.boxplot(data=df_train, x="verification_status", y="annual_inc")
# With this graph is hard to see the relationship
# Maybe we need the log of annual_inc
df_train_temp = df_train.copy()
df_train_temp["annual_inc_log"] = np.log(df_train_temp["annual_inc"])
sns.boxplot(data=df_train_temp, x="verification_status", y="annual_inc_log")
# It seems that the relationship between annual_inc and verification_status
# is not so clear cut.
# My hypothesis was not verified by the empirical test.

# In[ ]:
df_train["purpose"].value_counts()
# there are 14 categories
# some of the categories have few cases
df_train["purpose"].hist(bins=40)
# On the two-dimensional analysis we see how the 
# feature and the target variable behave
# In[ ]:
df_train["title"].value_counts()
# There are 48,815 different titles
# This is another case of categorical variable 
# with too many categories. 
# And that doesn't have a natural order.
# In[ ]:
# dti: is an index that ponders the monthly debt payment divided by total income
# So the lower the value the better I imagine
# We'll need to see on the bivariate analysis.
df_train["dti"].hist(bins=60)
# In[ ]:
df_train.head()
df_train["earliest_cr_line"]
# For now this is a date variable,
# But for our purposes we'll use this feature as a categorical
# ordered feature.

df_train["earliest_cr_line"].value_counts()
# number of different categories: 645
# Maybe we'll need to group this variable into bigger groups
# Idea: The feature engineering function will receive a string
# and with this it will output a number or a vector of numbers

# Notes about the preprocessing functions:
# Some scenarios about the preprocessing function:
# it receives a string, then it outputs an array.
# For example: 
# input = "Jun-1990"
# output = np.array([0, 0, 1, 0, 0, 0])
# In this case the string is a category, and we need to pass it
# into a one-hot enconding function.
#
# But there are cases where the preprocessing function is just
# something like:
# input = 29.1
# output = 0.34
# In here we maybe passing a MinMaxScaler at the input.
# 
# But at the end the .predict of the model
# we'll need to receive a np.array or a pd.Series/DataFrame
# For example Keras only accepts np.array, but sklearn also accepts
# pd.Series or pd.DataFrame
# But for universality it is better to us just np.array.

# In[ ]:

# to see the meaning of the variable
# df_metadata.loc["open_acc",:][0]

# "The number of open credit lines in the borrower's credit file."
df_train.head()
df_train["open_acc"].value_counts()
df_train["open_acc"].hist(bins=60)
# This is a numeric continuous variable 
# (it can be considered categorical with order)
# There are some values have too few of them
# 
# We have two options here, we can treat this variable
# (1) as a continuous variable, or treat the variable
# (2) as a order categorical variable
# 
# We can have different approaches for treatment for those two cases.
# If we adopt "open_acc" as a continuous variable we just leave the variable
# as it is. Later on we'll need to pass it onto a standardization step.
# For example, MinMaxScaler or StandardScaler.
# The variable "open_acc" have the ratio property
# if this property is very important we'll need to use the variable 
# as in approach (1) a continuous variable.
# The justification for using scalers is that it is better for convergence. 
# A more fundamental question is: how can we convert the values of the 
# parameters into interpretable values?
# By how much can we increase the speed of convergence or even the 
# probability of convergence by using scalers?
# For example, 80 for the variable "open_acc" is an outlier.
# What happens if we keep the outlier?
# How this can affect the model performance? Or convergence speed?
# When we adopt approach (2), we can groupe the outliers into 
# larger groups. That way we are kind of getting reed of outliers.
# But approach (2) seems to destroy information by deleting more
# detailed information about the variable.
# If the variable is considered a ordered categorical, we have two options:
# (a) use one-hot enconding, or (b) we can give integer numerical values
# to the groups. Using approaches (a) or (b) we'll need to apply a scaler.
# That is if we are adopting a model that needs scalers, for example ANN or 
# Linear Regressions. 
# Actually for linear regression or even GAM/GLM we can opt to do scaling 
# because one the advantages of using the features variables as they are 
# is that we can interpret the values of the beta coefficients 
# (excluding some types of GAMs).
# 
# Maybe in the case of a categorical ordered variable
# we should do the following steps:
# apply index int to the groups then apply a scaler.
# 
# Questions that can arise in thise settings: Which one is better to use
# Option (1) or option (2)?
# Better in the sense of model performance, and convergence speed.
# 
# 
df_train["open_acc"].value_counts().sort_index()

# In[ ]:
# pub_rec: 'Number of derogatory public records'
df_train.head()
df_train["pub_rec"].hist(bins=60)
df_train["pub_rec"].value_counts()
# df_metadata.loc["pub_rec",:][0]
# this is another variable that we can thing more if we can treat as a 
# a continuous numeric variable or we adopt the approach of a ordered 
# categorical variable.
# Maybe given that the great majority of cases are of value 0
# and just a few of them are greater than 4 we could use this variable
# as a categorical ordered variable.
# The variable "pub_rec" is a ratio numeric variable that is
# the distance between the values contain some information about the 
# phenomenon.
# For example to transform this variable into a categorical ordered one
# where we use integers to represent the categories 
# may not be appropriate for the case
# where the model been used is e.g. a linear regression model. 
# Because in linear regression the distance in the feature is relevant.
# But if we transform this variable into a categorical one with one-hot enconding
# I think it is ok to use linear regression.
# For example if we use this variable as an ordered categorical variable with 
# ordered integers. We could use random forests or any other tree based model.

# In[ ]:
# revol_bal: 'Total credit revolving balance'
df_train.head()
df_train["revol_bal"].hist(bins=60)
# this variable is skewed to the right.
# df_metadata.loc["revol_bal",:][0]
df_train["revol_bal"].value_counts()
# there are 49424 different types of values in this variable
# This is clearly a continuous numeric variable.
# What are the possible scalers that we can use?
# - MinMaxScaler
# - StandardScaler
# - RobustScaler
# - QuantileTransformer
# - Normalizer
# For this type of data which is the most appropriate?
# I would use some type of scaler for this variable, in principle I'd
# the MinMaxScaler for a starter, but I'd try to experiment 
# with other scaler functions.

# We can see patterns for feature engineering in tabular data.
# But can we automate it?
# Can we build a program that can make suggestions to what are the most
# interesting things to look at?
# This could take some work to do.
# The types of decision making for feature engineering follow
# I think a pattern, that maybe we can enconde in a software that
# can make suggestions to the user.

# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




