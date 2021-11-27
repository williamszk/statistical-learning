







# (110_647,)

# What is more important?
# The preduction ready of the model?
# Or the most performatic model?
# We should first try to build a pipeline, production ready code
# with focus on deployment.
# In most scenarios this is the priority order.
# But for research of the most performatic model
# this can be more flexible.
# Even in more flexible situations we should focus on trying 
# to give importance on how to serve the model.

# After building a production ready code we can 
# dedicate time for exploring the most performatic model.
# And new data will come and we'll need to observe the model drift
# and adapt the model for new scenarios.

df_train = pd.concat([df_features_train, df_target_train], axis=1)
df_train.head()
# For the EDA and the building of the feature engineering programs
# we should use the whole dataset as it is, with target and features
# together in a single data frame.
# 

# In the deploy simulation building we can imagine
# that the data is coming as dictionaries/json, this is not a 
# strong assumption. Most probably they will come, it depends
# on the backend of the firm's and how the get request responds.

# On the real deployment, we use absolutely all data that we have.
# But for studying and understanding the phonemenon we should make the
# separation of data into training and test, and we should do this
# in a most similar way to the deployment scenario as possible.

#%%
# What are the types of features that we have?
# or even that exist?
# 1. We have numeric, which have an order.
# 2. We have categorical with some natural order.
# 3. And we have categorical without an order.
# Are there any time/space features?
# Are there other types of information that can be considered like time and space?

df_train["loan_amnt"].hist(bins=60)
df_train["term"].hist()
df_train["int_rate"].hist(bins=60)
df_train["installment"].hist(bins=60)
df_train.head()
# Strategy for rapid iteration and value generation of the
# modelling effort:
# We try to run the model with just a subset of the features.
# We first see the most correlated variables with the target_variable.
# And use them as features.

# We need to transform the target_variable into a numeric variable
df_train[target_variable].hist()

# The variable below will be used for model training.
loan_status_numeric = np.array([
    hs.convert_loan_status_into_numeric(x) for x in df_train[target_variable]])
# All the functions that make some transformation of the 
# data should take individual values instead of for example
# using function that transform the whole data frame.
# That is, functions that have as arguments pd.DataFrame
# and the output pd.DataFrames. 
# But what we should do is to build functions that
# have arguments that are of primitive datatypes,
# and as outputs also primitive datatypes.

# For the test dataset we should simulate as if it was
# coming from the outside so we should separate the training
# from test dataset since the beginning before starting anything
# this will make the analysis and the challenge more difficult
# but it will simulate a situation of deployment.
# By the time that we use the test dataset, we'll need to think 
# how to preprocess the incoming data, so that it can be consumed 
# the .predict of the trained model.

#%%
df_train.head()
df_train["grade"].hist(bins=30)

#%%
plt.figure(figsize=(12, 6))
df_train["sub_grade"].hist(bins=70)
# %%
plt.figure(figsize=(12, 6))
df_train["emp_title"].value_counts()

# Teacher                               2606
# Manager                               2377
# Registered Nurse                      1171
# RN                                    1084
# Supervisor                             990
#                                       ... 
# Baxter Springs KS  USD#508 Schools       1
# Regional Adviser                         1
# Forcht Bank                              1
# Pipeline Manager                         1
# CarenetLA                                1
# Name: emp_title, Length: 143694, dtype: int64

# We have 143_694 different employee titles.
# This number is too high.
# This is a situation where we have too many different
# types of categorical non-ordered feature.
# I worked with this type of data in the 
# insurance industry.
# We can also find a feature with too many
# categories and that have some kind of ordering.

# If we're going to use this feature, first we'll 
# need to make some kind of grouping. 
# For this we could use PCA or other type of
# unsupervised learning method (?).
# Another method that we could use is by
# ordering the features according to how 
# the mean (or other measure) in relation to the 
# target variable changes. We could make some 


# emp_title is an example of a categorical variable
# that does not have an order.
# We have two options when using this type of features:
# 1. Transform into integer; or 
# 2. Do one-hot enconding.
# To 

# %%
