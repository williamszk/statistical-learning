# https://www.youtube.com/watch?v=ELE2_Mftqoc&ab_channel=freeCodeCamp.org
# this video is really bad

# q learning
# Deep Q Learning

# learning from the environment
# epsolon
# greedy, exploration

# Q learning is a reinforcement leraning algorithm
# not necessarily Q learning needs neural networks
# but it can use, and this is called deep Q learning

# Evaluation Network
# Target Network

# Reiforcement Learning Agent

# Convolution Neural Network: CNN 
# is used for extracting features from images

# Dense Neural Network

# Stack Frames to give the RL agent a sense of motion

# The CNN uses a stack of images instead of a single image


# Difference between reinforcement learning (RL) and supervised learning (SL)
# Labeled data comes from humans

# RL uses goals instead of targets
# 

#%%
import os
import numpy as np
import tensorflow as tf

#%%

class DeepQNetwork(object):
    def __init__(self, learning_rate, n_actions, name,
    fcl_dims=256, input_dims=(210, 160, 4), 
    checkpoint_dir = "../models/"
    ) -> None:
        self.learning_rate = learning_rate
        self.n_actions = n_actions
        self.name = name
        self.fcl_dims = fcl_dims
        self.input_dims = input_dims
        self.checkpoint_dir = checkpoint_dir
        self.session = tf.Session()
        self.build_network()
        self.session.run(tf.global_variables_intializer())
        self.saver = tf.train.Saver()
        self.checkpoint_file = os.path.join(checkpoint_dir, "deepqnet.ckpt")
        self.params = tf.get_collection(
            tf.GraphKeys.TRAINABLE_VARIABLES, 
            scope=self.name
        )

    def build_network(self):
        with tf.variable_scope(self.name):
            self.input = tf.compat.v1.placeholder(tf.float32, shape=[None, *self.input_dims],
                name="inputs"
            )
            self.actions = tf.compat.v1.placeholder(tf.float32, shape=[None, *self.n_actions],
                name="action_taken"
            )
            self.q_target = tf.compat.v1.placeholder(tf.float32, shape=[None, *self.n_actions])

            convolutional_1 = tf.compat.v1.layers.conv2d(inputs=self.input, filters=32, kernel_size=(8,8),
                strides=4, name="convolutional_1", 
                kernel_initializer=tf.compat.v1.variance_scaling_initializer(scale=2)
                )
            
            convolutional_1_activated = tf.compat.v1.nn.relu(convolutional_1)

            convolutional_2 = tf.compat.v1.layers.conv2d(
                inputs=convolutional_1_activated, 
                filters=64, 
                kernel_size=(4,4), 
                strides=2, 
                name="convolutional_2",
                kernel_initializer=tf.compat.v1.variance_scaling_initializer(scale=2)
                )
            
            convolutional_2_activated = tf.compat.v1.nn.relu(convolutional_2)

            convolutional_3 = tf.compat.v1.layers.conv2d(
                inputs=convolutional_2_activated,
                filters=28,
                kernel_size=(3,3),
                strides=1,
                name="convolutional_3",
                kernel_initializer=tf.compat.v1.variance_scaling_initializer(scale=2)
                )
            
            convolutional_3_activated = tf.compat.v1.nn.relu(convolutional_3)

            flat = tf.compat.v1.layers.flatten(convolutional_3_activated)
            dense_layer = tf.compat.v1.layers.dense(
                flat, 
                units=self.fcl_dims,
                activation=tf.compat.v1.nn.relu,
                kernel_initializer=tf.compat.v1.variance_scaling_initializer(scale=2)
            )

            self.Q_values = tf.compat.v1.layers.dense(
                dense_layer,
                units=self.n_actions,
                kernel_initializer=tf.compat.v1.variance_scaling_initializer(scale=2)
                )

            self.q_paramter = tf.compat.v1.reduce_sum(
                tf.compat.v1.multiply(
                    self.Q_values, 
                    self.actions
                    )
            )

            self.loss_function = tf.compat.v1.reduce_mean(
                tf.compat.v1.square(self.q_paramter - self.q_target)
                )

            self.train_operation = tf.compat.v1.train.AdamOptimizer(
                self.learning_rate
            ).minimize(self.loss_function)

    def load_checkpoint(self):
        print("... loading checkpoint ...")
        self.saver.restore(
            self.session, 
            self.checkpoint_file
            )

    def save_checkpoints(self):
        print("... saving checkpoint ...")
        self.saver.save(
            self.session,
            self.checkpoint_file
        )

class Agent(object):
    def __init__(
        self,
        alpha_parameter,
        gamma_parameter,
        memory_size,
        n_actions,
        epsilon_parameter,
        batch_size,
        replace_target=5000,
        input_dimensions=(210, 160, 4),
        q_next="../models/q_next",
        q_evaluation="../models/q_evaluation"
        ) -> None:
        super().__init__()

#%%



#%%


















