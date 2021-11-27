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
# pd.read_csv("../data/lending_club_info.csv", index_col="LoanStatNew")
df_00 = pd.read_csv("../data/lending_club_loan_two.csv")
df_00


# In[4]:


# which is the target variable?
target_variable = "loan_status"
# this is one of the most important things to determine
# when we are working with a supervised learning problem


# In this dataset we have a variable that tells when the loan was issued: `issue_d`. 
# 
# To simulate a scenario of new loans coming we should split according to time. 
# 
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
# 
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
#     train_test_split(df_features, df_target, test_size=0.25, random_state=42)


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
# 
# The production ready of the model?
# 
# Or the most performatic model?
# 
# We should first try to build a pipeline, production ready code with focus on deployment.
# 
# In most scenarios this is the priority order.
# 
# But for research of the most performatic model is more relevant, and this priority level can be more flexible.
# 
# Even in more flexible situations we should focus on trying  to give importance on how to serve the model.

# After building a production ready code we can  dedicate time for exploring the most performatic model.
# 
# And new data will come and we'll need to observe the model drift and adapt the model for new scenarios.

# In[20]:


# join the features and the target variable again
df_train = pd.concat([df_features_train, df_target_train], axis=1)
df_train.head()


# For the EDA and the building of the feature engineering programs we should use the whole dataset as it is, with target and features together in a single data frame.
# 
# In the deployment simulation construction we can imagine that the data is coming as dictionaries/json, this is not a  strong assumption. 
# 
# Most probably the data will arrive in this format, but this depends on the backend of the firm and how the get request responds.

# On the real deployment, we use absolutely all data that we have.
# 
# But for studying and understanding the phonemenon we should make the separation of data into training and test, and we should do this in a most similar way to the deployment scenario as possible.

# What are the types of features that we have?
# 
# Or even that exist?
# 
# 1. We have numeric, which have an order.
# 2. We have categorical with some natural order.
# 3. And we have categorical without an order.
# 
# Are there any time/space features?
# 
# Are there other types of information that can be considered like time and space?

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
# 
# We try to run the model with just a subset of the features.
# 
# We first see the most correlated variables with the target_variable.
# 
# And use them as features. In this way we can have a benchmark. We can keep track of the progress of the model.

# In[26]:


# We need to transform the target_variable into a numeric variable
df_train[target_variable].hist()


# In[28]:


# The variable below will be used for model training.
loan_status_numeric = np.array([
    hs.convert_loan_status_into_numeric(x) for x in df_train[target_variable]])
loan_status_numeric


# All the functions that make some transformation of the data should take individual values instead of for example using function that transform the whole data frame.
# 
# That is, functions that have as arguments `pd.DataFrame` and the output `pd.DataFrames`, shouldn't be used/created.
# 
# What we should do is to build functions that have arguments that are of primitive datatypes (int, str, float), and as outputs also primitive datatypes.

# For the test dataset we should simulate as if it was coming from the outside world. 
# 
# So we should separate the training from test dataset since the beginning of our analysis. 
# 
# That is, before starting anything, this will make the analysis and the challenge more difficult but it will simulate a situation of deployment.
# 
# By the time that we use the test dataset, we'll need to think  how to preprocess the incoming data, so that it can be consumed the `.predict` of the trained model.

# In[29]:


# grade: loan grade
df_train["grade"].hist(bins=30)
# I imagine that A is better than B, and so on...


# In[31]:


# sub_grade: 
plt.figure(figsize=(14, 6))
df_train["sub_grade"].hist(bins=70)


# In[33]:


# emp_title: the job title that the borrower told when applying for the loan
plt.figure(figsize=(12, 6))
df_train["emp_title"].value_counts()


# We have 143_694 different employee titles.
# 
# This number is too high.
# 
# This is a situation where we have too many different types of categorical non-ordered feature.
# 
# I worked with this type of data in the insurance industry. (I should revisit the code that I used there to see the methods that I wrote to automatically group the categories that are too sparce)
# 
# We can also find a feature with too many categories and that have some kind of ordering.

# If we're going to use this feature, first we'll need to make some kind of grouping. 
# 
# For this we could use PCA or other type of unsupervised learning method (?).
# 
# Another method that we could use is by ordering the features according to how  the mean (or other measure) in relation to the target variable changes. 
# 

# `emp_title` is an example of a categorical variable that does not have an order.
# 
# We have two options when using this type of features:
# 
# 1. Transform into integer; or 
# 2. Do one-hot enconding.
# 
# 

# - I am thinking about writing some examples of practical methods for dealing with data.
# 
# - But we also need to remember that the data that we see here are for problems that are for tabular data. 
# 
# - I say "tabular data" in a way to differentiate for example to problems like: image classification, NLP, and reiforcement learning.
# 
# - The methods of ANN can be used for tabular data problems. So deep learning can be used for tabular data problems.
# 
# - Inside tabular data problems we can have supervised (regression, classification) problems, and also unsupervised problems. 
# 
# - Maybe there is another name, a better name instead of tabular data problems. 
# 
# - I use this term in a sense to differentiate these types of problems from the other machine learning problems: NLP, image and sound processing, and RL.

# - Thinking about the steps that we need to take when making EDA and feature engineering.
# 
# - I think that mostly there is an art to it. That is there is not set of steps that are perfect for EDA or even for feature engineering. Nothing that I saw. But those are interesting to study and apply.
# 
# - I notice that the first thing that we need to do in a new dataset is to go through each variable that we have and understand its meaning, its meaning in the sense of the business or the domain problem.
# 
# - We need to answer questions like:
# 
# - How this data is generated, and how is this applied to our problem?
# 
# - Make a histogram of the variable.
# 
# - Make a table of frequency of the variable.
# 
# - Verify if the variables is numeric or string. 
# 
# - If the variable is categorical, is categorical with some natural order? Or it doesn't have an order?
# 
# - If the variable is categorical and with order, does the distance between each category have some intrinsic meaning? If it does than maybe this is a numeric discrete variable.
# 
# - If the variable is numeric the distance between the values have some meaning? If it does (there is a name for this)
# 
# - If the variable is categorical but the distance doesn't have meaning, this variable can be just a categorical with ordering.
# 
# - The variable can be a number but there is no order in them, for example zip code.
# 
# 

# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




