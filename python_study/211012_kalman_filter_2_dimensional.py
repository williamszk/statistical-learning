#%%
import numpy as np
from numpy.linalg import inv
import pandas as pd
import seaborn as sns
sns.set()

# experiment with 1 dimensional series
# the z time series is a random walk
#%%
np.random.seed(42)

z1_0 = np.random.randn()
z2_0 = np.random.randn()
z1_time_series = [z1_0]
z2_time_series = [z2_0]

len_z_series = 100

for i in range(len_z_series-1):
    z1_time_series.append(z1_time_series[i] + np.random.randn())
    z2_time_series.append(z2_time_series[i] + np.random.randn())

z_time_series = [np.array([z1, z2]) for z1, z2 in zip(z1_time_series, z2_time_series)]

pd.Series(z1_time_series).plot()
pd.Series(z2_time_series).plot()
#%%
# build a kalman filter for this series
x_0 = np.array([z1_time_series[0], z2_time_series[0]])

# a list of np.arrays
x_signal_series = [x_0]

P_0 = np.identity(2)*2
Q = np.identity(2)*2
R = np.identity(2)*10
H = np.identity(2)

# for matrix multiplication in numpy
# np.array([[1,2],[3,4]]).dot(np.array([[1,2],[3,4]]))
# numpy transpose of matrix
# np.array([[1,2],[3,4]]).transpose()
# inv(np.array([[1,2],[3,4]]))

t = 1
for t in range(1, len_z_series):
    # just for initial values
    if t == 1:
        x_t1 = x_0
        P_t1 = P_0

    # prediction step
    x_t = x_t1
    P_t = P_t1 + Q
    z_t = z_time_series[t]

    # correction step
    K_t = P_t.dot(H).dot(inv(H.dot(P_t).dot(H.transpose()) + R))
    x_t_c = x_t + K_t.dot(z_t - x_t)
    P_t_c = (np.identity(2) - K_t).dot(P_t)

    x_signal_series.append(x_t_c)

    x_t1 = x_t_c
    P_t1 = P_t_c

#%%
df_time_series = pd.DataFrame({
    "z1_time_series": [x[0] for x in z_time_series],
    "z2_time_series": [x[1] for x in z_time_series],
    "x1_signal_series": [x[0] for x in x_signal_series],
    "x2_signal_series": [x[1] for x in x_signal_series]
    })

df_time_series.plot()
#%%






