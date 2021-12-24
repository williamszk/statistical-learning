# Take the package gym, google it, see another problem to solve
# and with what we already know try to solve another problem with Q-learning.

import gym


env = gym.make("CartPole-v1")
env.reset()
env.observation_space.high
env.observation_space.low
env.action_space.n
# there are 2 possible actions
# go to the left or right

DISCRETE_SIZE = [10]*len(env.observation_space.high)
# in many situation we don't know the values here
# the difficult part is to able to characterize the environment
# to understand which are the values that we can get
# and how the environmnet respond to the agent's action
discrete_window_size = (env.observation_space.high - env.observation_space.low)/DISCRETE_SIZE
# there are two observation space fields that are infinite






done = False
done_counter = 0
for i_episode in range(20):
    observation = env.reset()
    while not done:
        env.render()
        action = env.action_space.sample()
        new_observation, reward, done, _ = env.step(action)
        print(new_observation, reward, done)



env.close()





# we can take a look at the docs for more information
# https://gym.openai.com/docs/

# how to find all environments
gym.envs.registry.all()
# dict_values([
#  EnvSpec(CartPole-v0), 
#  EnvSpec(CartPole-v1), 
#  EnvSpec(MountainCar-v0),
#  EnvSpec(MountainCarContinuous-v0),
#  EnvSpec(Pendulum-v1),
#  EnvSpec(Acrobot-v1),
#  EnvSpec(LunarLander-v2),
#  EnvSpec(LunarLanderContinuous-v2),
#  EnvSpec(BipedalWalker-v3),
#  EnvSpec(BipedalWalkerHardcore-v3),
#  EnvSpec(CarRacing-v0),
#  EnvSpec(Blackjack-v1),
#  EnvSpec(FrozenLake-v1),
#  EnvSpec(FrozenLake8x8-v1),
#  EnvSpec(CliffWalking-v0),
#  EnvSpec(Taxi-v3),
#  EnvSpec(Reacher-v2),
#  EnvSpec(Pusher-v2),
#  EnvSpec(Thrower-v2),
#  EnvSpec(Striker-v2),
#  EnvSpec(InvertedPendulum-v2),
#  EnvSpec(InvertedDoublePendulum-v2),
#  EnvSpec(HalfCheetah-v2),
#  EnvSpec(HalfCheetah-v3),
#  EnvSpec(Hopper-v2),
#  EnvSpec(Hopper-v3),
#  EnvSpec(Swimmer-v2),
#  EnvSpec(Swimmer-v3),
#  EnvSpec(Walker2d-v2),
#  EnvSpec(Walker2d-v3),
#  EnvSpec(Ant-v2),
#  EnvSpec(Ant-v3),
#  EnvSpec(Humanoid-v2),
#  EnvSpec(Humanoid-v3),
#  EnvSpec(HumanoidStandup-v2),
#  EnvSpec(FetchSlide-v1),
#  EnvSpec(FetchPickAndPlace-v1),
#  EnvSpec(FetchReach-v1),
#  EnvSpec(FetchPush-v1),
#  EnvSpec(HandReach-v0),
#  EnvSpec(HandManipulateBlockRotateZ-v0),
#  EnvSpec(HandManipulateBlockRotateZTouchSensors-v0),
#  EnvSpec(HandManipulateBlockRotateZTouchSensors-v1),
#  EnvSpec(HandManipulateBlockRotateParallel-v0),
#  EnvSpec(HandManipulateBlockRotateParallelTouchSensors-v0),
#  EnvSpec(HandManipulateBlockRotateParallelTouchSensors-v1),
#  EnvSpec(HandManipulateBlockRotateXYZ-v0),
#  EnvSpec(HandManipulateBlockRotateXYZTouchSensors-v0),
#  EnvSpec(HandManipulateBlockRotateXYZTouchSensors-v1),
#  EnvSpec(HandManipulateBlockFull-v0),
#  EnvSpec(HandManipulateBlock-v0),
#  EnvSpec(HandManipulateBlockTouchSensors-v0),
#  EnvSpec(HandManipulateBlockTouchSensors-v1),
#  EnvSpec(HandManipulateEggRotate-v0),
#  EnvSpec(HandManipulateEggRotateTouchSensors-v0),
#  EnvSpec(HandManipulateEggRotateTouchSensors-v1),
#  EnvSpec(HandManipulateEggFull-v0),
#  EnvSpec(HandManipulateEgg-v0),
#  EnvSpec(HandManipulateEggTouchSensors-v0),
#  EnvSpec(HandManipulateEggTouchSensors-v1),
#  EnvSpec(HandManipulatePenRotate-v0),
#  EnvSpec(HandManipulatePenRotateTouchSensors-v0),
#  EnvSpec(HandManipulatePenRotateTouchSensors-v1),
#  EnvSpec(HandManipulatePenFull-v0),
#  EnvSpec(HandManipulatePen-v0),
#  EnvSpec(HandManipulatePenTouchSensors-v0),
#  EnvSpec(HandManipulatePenTouchSensors-v1),
#  EnvSpec(FetchSlideDense-v1),
#  EnvSpec(FetchPickAndPlaceDense-v1),
#  EnvSpec(FetchReachDense-v1),
#  EnvSpec(FetchPushDense-v1),
#  EnvSpec(HandReachDense-v0),
#  EnvSpec(HandManipulateBlockRotateZDense-v0),
#  EnvSpec(HandManipulateBlockRotateZTouchSensorsDense-v0),
#  EnvSpec(HandManipulateBlockRotateZTouchSensorsDense-v1),
#  EnvSpec(HandManipulateBlockRotateParallelDense-v0),
#  EnvSpec(HandManipulateBlockRotateParallelTouchSensorsDense-v0),
#  EnvSpec(HandManipulateBlockRotateParallelTouchSensorsDense-v1),
#  EnvSpec(HandManipulateBlockRotateXYZDense-v0),
#  EnvSpec(HandManipulateBlockRotateXYZTouchSensorsDense-v0),
#  EnvSpec(HandManipulateBlockRotateXYZTouchSensorsDense-v1),
#  EnvSpec(HandManipulateBlockFullDense-v0),
#  EnvSpec(HandManipulateBlockDense-v0),
#  EnvSpec(HandManipulateBlockTouchSensorsDense-v0),
#  EnvSpec(HandManipulateBlockTouchSensorsDense-v1),
#  EnvSpec(HandManipulateEggRotateDense-v0),
#  EnvSpec(HandManipulateEggRotateTouchSensorsDense-v0),
#  EnvSpec(HandManipulateEggRotateTouchSensorsDense-v1),
#  EnvSpec(HandManipulateEggFullDense-v0),
#  EnvSpec(HandManipulateEggDense-v0),
#  EnvSpec(HandManipulateEggTouchSensorsDense-v0),
#  EnvSpec(HandManipulateEggTouchSensorsDense-v1),
#  EnvSpec(HandManipulatePenRotateDense-v0),
#  EnvSpec(HandManipulatePenRotateTouchSensorsDense-v0),
#  EnvSpec(HandManipulatePenRotateTouchSensorsDense-v1),
#  EnvSpec(HandManipulatePenFullDense-v0),
#  EnvSpec(HandManipulatePenDense-v0),
#  EnvSpec(HandManipulatePenTouchSensorsDense-v0),
#  EnvSpec(HandManipulatePenTouchSensorsDense-v1),
#  EnvSpec(CubeCrash-v0),
#  EnvSpec(CubeCrashSparse-v0),
#  EnvSpec(CubeCrashScreenBecomesBlack-v0),
#  EnvSpec(MemorizeDigits-v0)])