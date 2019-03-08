# coding=UTF-8

import numpy as np
import tensorflow as tf

# create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3

# build structure
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))
y = x_data * Weights + biases

# calculate loss and spread loss
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# start train
init = tf.global_variables_initializer()  # init variable (very important)
with tf.Session() as sess:
    sess.run(init)  # activate variable
    for step in range(201):
        sess.run(train)  # activate func
        if step % 20 == 0:
            print(step, sess.run(Weights), sess.run(biases))  # 直接打印无效，需要将sess的指针放到这里run一下
