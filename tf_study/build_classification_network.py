# coding=utf-8

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs


def compute_accuracy(t_xs, t_ys):
    global prediction
    y_pre = sess.run(prediction, feed_dict={xs: t_xs})
    correct_prediction = tf.equal(tf.argmax(y_pre, 1), tf.argmax(t_ys, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    result = sess.run(accuracy, feed_dict={xs: t_xs, ys: t_ys})
    return result


# 准备数据，MNIST库是手写体数字库
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

# 搭建网络：inputs - layer - loss/train
# 1、inputs
xs = tf.placeholder(tf.float32, [None, 784])  # 28x28
ys = tf.placeholder(tf.float32, [None, 10])

# 2、layer
prediction = add_layer(xs, 784, 10, activation_function=tf.nn.softmax)

# 3、loss/train
cross_entropy_loss = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction), reduction_indices=[1]))
train = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy_loss)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(1000):
        batch_xs, batch_ys = mnist.train.next_batch(100)  # 每次取100张图片进行训练
        sess.run(train, feed_dict={xs: batch_xs, ys: batch_ys})
        if i % 50 == 0:
            print(compute_accuracy(mnist.test.images, mnist.test.labels))  # 测试数据与预测数据比较，计算精确度(%)
