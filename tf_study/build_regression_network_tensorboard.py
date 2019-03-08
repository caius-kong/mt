# coding=UTF-8
import numpy as np
import tensorflow as tf


# 添加神经层函数
def add_layer(inputs, in_size, out_size, layer_name, activation_function=None):
    with tf.name_scope(layer_name):
        # 定义一个随机变量矩阵 和 0向量+0.1的向量
        with tf.name_scope('Weights'):
            Weights = tf.Variable(tf.random_normal([in_size, out_size]), name='W')
            tf.summary.histogram(layer_name + '/Weights', Weights)
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, name='b')
            tf.summary.histogram(layer_name + '/biases', biases)
        # 我们的预测值
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.matmul(inputs, Weights) + biases
        # 如果没有激励函数，则线性关系，否则非线性关系
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        tf.summary.histogram(layer_name + '/outputs', outputs)
        return outputs


# 准备真实数据（一元二次函数）
x_data = np.linspace(-1, 1, 300, dtype=np.float32)[:, np.newaxis]  # -1 ~ 1之间300个数值
noise = np.random.normal(0, 0.05, x_data.shape).astype(np.float32)  # 为了使数据更加真实，加上噪点
y_data = np.square(x_data) - 0.5 + noise

# 定义我们所需的神经网络的输入
with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32, [None, 1], name='x_input')  # None表示随意输入多少， 1代表特征数
    ys = tf.placeholder(tf.float32, [None, 1], name='y_input')

# 搭建神经网络，简单的三层模型 —— 假定输入输出数：输入层1个、隐藏层10个、输出层1个
hl1 = add_layer(xs, 1, 10, 'hidden_layer', activation_function=tf.nn.relu)  # 隐藏层，hl1表示隐藏层输出
prediction = add_layer(hl1, 10, 1, 'outputs', activation_function=None)  # 输出层，prediction表示输出层输出（预测值）
with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]))  # 真实输出与预测输出误差
    tf.summary.scalar('loss', loss)
with tf.name_scope('train'):
    train = tf.train.GradientDescentOptimizer(0.1).minimize(loss)  # 梯度下降优化器优化精度（学习率为0.1）

# 开始训练
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    writer = tf.summary.FileWriter("logs/", sess.graph)
    merged = tf.summary.merge_all()  # 打包所有图层
    for i in range(1000):
        # training
        sess.run(train, feed_dict={xs: x_data, ys: y_data})
        if i % 50 == 0:
            # 计算图层，并写入
            result = sess.run(merged, feed_dict={xs: x_data, ys: y_data})
            writer.add_summary(result, i)
