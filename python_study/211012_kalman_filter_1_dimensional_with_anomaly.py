#%%
"""
An experiment:

A 1-dimensional random walk time series, with KF applied.

"""

import numpy as np
import pandas as pd
from copy import deepcopy
from typing import List
import seaborn as sns
sns.set()
from IPython.display import display, Markdown, Latex

# experiment with 1 dimensional series
# the z time series is a random walk
#%%
np.random.seed(42)

z_0 = np.random.randn()
z_time_series = [z_0]

len_z_series = 100

for i in range(len_z_series-1):
    z_time_series.append(z_time_series[i] + np.random.randn())

z_pandas_series = pd.Series(z_time_series)
z_pandas_series.plot()

df_original = pd.DataFrame({
    "x_series":z_time_series,
    "time":range(len(z_time_series))
})

#%%
# The graph above is the random generated random walk that we
# are going to fit a model on.

# display(Markdown(
#     "The graph above is the random generated random walk that we"
#     "are going to fit a model on."))
# display(Markdown('*some markdown* $\phi$'))
# display(Latex('$\phi$'))
#%%
display(Latex(
    "$\phi$"
    ))

#%%
display(Latex(
    "$$ x_k^{-} = x_{k-1}^{+} $$"
    "$$ P_k^{-} = P_k^{+} $$"
    "$$ P_k^{-} = P_k^{+} $$"
    ))

#%%
# build a kalman filter for this series
x_0 = z_pandas_series[0]
x_signal_series = [x_0]
P_0 = 10
Q = 1
R = 1

for t in range(1, len_z_series):
    # just for initial values
    if t == 1:
        x_t1 = x_0
        P_t1 = P_0

    # prediction step
    x_t = x_t1
    P_t = P_t1 + Q
    z_t = z_pandas_series[t]

    # correction step
    K_t = P_t/(P_t + R)
    x_t_c = x_t + K_t*(z_t - x_t)
    P_t_c = (1 - K_t)*P_t

    x_signal_series.append(x_t_c)

    x_t1 = x_t_c
    P_t1 = P_t_c

df_time_series = pd.DataFrame({
    "z_time_series": z_time_series,
    "x_signal_series": x_signal_series})

df_time_series.plot()
# 
#%%
# Above in orange we have the signal extracted with Kalman Filter from a single variable
# time series.
#%%
# Here we generate anomalies in the time series an observe how 
# the signal will behave.

# first we just let the signal capture the anomaly
# and let it use in the correction step

#%%
original_array = np.array(z_time_series)
time_array = np.array(range(len(z_time_series)))
start = 0.2
delta_delay = 0.1

df_00 = pd.DataFrame({
    "x_series": original_array,
    "time": time_array})

#%%
def constant_delay(df_00: pd.DataFrame, start: float, delta_delay = 0.1) -> pd.DataFrame:
    
    list_bsms_2 = np.array(df_00["x_series"]).copy()
    time_array = np.array(df_00["time"]).copy()

    start_timestamp = np.quantile(time_array, start)
    end_interval_timestamp = np.quantile(time_array, start + delta_delay)
    index_start = np.sum(time_array < start_timestamp)

    qtd_delete = np.sum(
        (start_timestamp < time_array) &  
        (time_array < end_interval_timestamp))

    list_bsms_3 = list(list_bsms_2[0:index_start]) +\
        list(list_bsms_2[(index_start + qtd_delete):])

    time_array_2 = time_array.copy()
    time_delay = time_array_2[index_start+qtd_delete] - time_array_2[index_start]

    time_array_3 = list(time_array_2[0:index_start])+\
        list(time_array_2[(index_start + qtd_delete):] - time_delay)

    # create a vector that contains 1 and 0 for anomaly or not
    # this is used further for training purposes
    # we can later tell if an observation is an anomaly or not
    vector_labeled_anomaly = [1 if i >= index_start else 0 for i,_ in enumerate(time_array_3)]
    
    df_01 = pd.DataFrame({
        "x_series":list_bsms_3,
        "time":time_array_3,
        "anomalous_label":vector_labeled_anomaly
    })

    return df_01

#%%
df_01 = constant_delay(df_00, 0.5)
df_01.index = df_01["time"]
df_01.loc[:,["x_series"]].plot()
# sns.scatterplot(x="time", y="x_series", data=df_01)
sns.scatterplot(x="time", y="x_series", data=df_01, hue="anomalous_label")
#%%

# the graph above show an example of anomalous data
# it does not seem to be but the orange data is anomalous

#%%

def find_kalman_filter(df_00: pd.DataFrame) -> pd.DataFrame:
    len_z_series = len(df_00)
    # build a kalman filter for this series
    z_pandas_series = df_00["x_series"]
    x_0 = z_pandas_series[0]
    x_signal_series = [x_0]
    P_0 = 10
    Q = 1
    R = 1

    for t in range(1, len_z_series):
        # just for initial values
        if t == 1:
            x_t1 = x_0
            P_t1 = P_0

        # prediction step
        x_t = x_t1
        P_t = P_t1 + Q
        z_t = z_pandas_series[t]

        # correction step
        K_t = P_t/(P_t + R)
        x_t_c = x_t + K_t*(z_t - x_t)
        P_t_c = (1 - K_t)*P_t

        x_signal_series.append(x_t_c)

        x_t1 = x_t_c
        P_t1 = P_t_c

    df_00["signal_series"] = x_signal_series

    return df_00
#%%
df_02 = find_kalman_filter(df_01)

df_02.loc[:, ["x_series", "signal_series"]].plot()


df_temp = find_kalman_filter(df_original)
df_temp.loc[:, ["x_series", "signal_series"]].plot()
#%%
# the first figure on the top show an example of kalman filter applied 
# to a series with anomaly of type constant_delay
# the second graph shows the original series, without the 
# anomaly applied