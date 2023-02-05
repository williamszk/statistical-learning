# https://www.intechopen.com/chapters/63164

"""
The objective here is to build the same specification from the article
above. 
The specification for velocity and acceleration.
"""

#%%
import numpy as np
import seaborn as sns
sns.set()

#%%
# simulate tranjectory of a rocket
np.random.seed(42)

coordinate_std = 2

len_trajectory = 100
time_array = range(len_trajectory)
x_coordinate = np.array(time_array) **1.3 + np.random.randn(len_trajectory)*coordinate_std
y_coordinate = np.array(time_array) **1.2 + np.random.randn(len_trajectory)*coordinate_std
z_coordinate = np.array(time_array) **2 + np.random.randn(len_trajectory)*coordinate_std

sns.relplot(x = time_array, y = x_coordinate)
sns.relplot(x = x_coordinate, y = y_coordinate)
sns.relplot(x = x_coordinate, y = z_coordinate)

#%%
np.random.seed(42)
velocity_std = 4
# create vectors of velocity in each dimension
# include noise into the velocity too

x_velocity = x_coordinate[]

