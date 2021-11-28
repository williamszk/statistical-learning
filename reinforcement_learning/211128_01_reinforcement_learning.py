# https://pythonprogramming.net/q-learning-reinforcement-learning-python-tutorial/
#%%
import gym

environment = gym.make("MountainCar-v0")
print(environment.action_space.n)
# it shows the number of actions possible in this environment

#%%
import gym

environment = gym.make("MountainCar-v0")
environment.reset()

done = False
while not done:
    action = 2 # always to to right
    environment.step(action)
    environment.render()

# this code will create a video showing how the
# state changes with the action

#%%


#%%


#%%


#%%


#%%


