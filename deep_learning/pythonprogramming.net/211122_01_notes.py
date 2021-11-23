
# https://pythonprogramming.net/q-learning-reinforcement-learning-python-tutorial/
#%%
import gym

environment = gym.make("MountainCar-v0")

environment.action_space.n

environment.reset()

done = False
while not done:
    action = 0
    environment.step(action)
    environment.render()


#%%
import gym

env = gym.make("MountainCar-v0")
print(env.reset())
type(env.reset())
#%%

import gym
env = gym.make("MountainCar-v0")
state = env.reset()

done = False
list_reward = []
while not done:
    action = 2
    new_state, reward, done, info = env.step(action)
    list_reward.append(reward)
    print(reward, new_state)

#%%
import pandas as pd
pd.Series(list_reward).plot()

#%%
















