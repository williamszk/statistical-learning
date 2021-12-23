# https://pythonprogramming.net/q-learning-reinforcement-learning-python-tutorial/
# https://www.youtube.com/watch?v=yMk_XtIEzH8&t=208s&ab_channel=sentdex
# https://www.youtube.com/watch?v=Gq1Azv_B4-4&ab_channel=sentdex
import gym
from gym.envs.registration import EnvRegistry
import numpy as np

environment = gym.make("MountainCar-v0")
environment.reset()

LEARNING_RATE = 0.1
DISCOUNT = 0.95
epsilon = 25_000
SHOW_EVERY = 500
epsilon = 0.5 # random action/exploratory parameter
START_EPSILON_DECAYING = 1
END_EPSILON_DECAYING = epsilon // 2
epsilon_decay_value = epsilon / (END_EPSILON_DECAYING - START_EPSILON_DECAYING)

# info about the environment the highest possible value
environment.observation_space.high
# array([0.6 , 0.07], dtype=float32)

# info about the environment the lowest possible value 
environment.observation_space.low
# array([-1.2 , -0.07], dtype=float32)

# in many situations we might not know what are those values

# number of actions possible
environment.action_space.n


DISCRETE_SIZE = [20]*len(environment.observation_space.high)
discrete_window_size = (environment.observation_space.high - environment.observation_space.low)/ DISCRETE_SIZE

q_table = np.random.uniform(low=-2, high=0, size=DISCRETE_SIZE+[environment.action_space.n])
q_table.shape


def get_discrete_state(state):
    """
    Example
    -------
    ```
    state = environment.reset()
    ```
    """
    discrete_state = (state - environment.observation_space.low) / discrete_window_size
    return tuple(discrete_state.astype(int))

# state = environment.reset()
discrete_state = get_discrete_state(environment.reset())

q_table[discrete_state]
np.argmax(q_table[discrete_state])
# which index have the highest value?

for episode in range(epsilon):
    if episode % SHOW_EVERY == 0:
        print(episode)
        render = True
    else:
        render = False

    discrete_state = get_discrete_state(environment.reset())
    done = False
    while not done:
        if np.random.random() > epsilon:
            action = np.argmax(q_table[discrete_state])
        else:
            action = np.random.randint(0, environment.action.n)

        new_state, reward, done, _ = environment.step(action)
        new_discrete_state = get_discrete_state(new_state)
        # print(reward, new_state)
        if render:
            environment.render()
        if not done:
            max_future_q = np.max(q_table[new_discrete_state])
            current_q = q_table[discrete_state + (action,)]
            
            new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
            q_table[discrete_state + (action,)] = new_q
        elif new_state[0] >= environment.goal_position:
            print(f"We made it on episode: {episode}")
            q_table[discrete_state + (action, )] = 0

        discrete_state = new_discrete_state

    if END_EPSILON_DECAYING >= episode >= START_EPSILON_DECAYING:
        epsilon -= epsilon_decay_value

environment.close()

# next video:
# https://www.youtube.com/watch?v=CBTbifYx6a8&ab_channel=sentdex


# Project ideas:
# 1. Take the package gym, google it, see another problem to solve
#   and with what we already know try to solve another problem with Q-learning.
# 2. Export the q_table and try to use it in another program and see how the 
#   model behaves, if it can always solve the problem.

















