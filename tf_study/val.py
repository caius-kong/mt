import tensorflow as tf

# 定义变量、常量
state = tf.Variable(0, name="counter")
one = tf.constant(1)
print(state, one)

# 定义加法步骤，并将 state 更新成 new_value
new_val = tf.add(state, one)
update = tf.assign(state, new_val)

# 初始化变量
init = tf.global_variables_initializer()
with tf.Session() as sess:
    # 激活变量 (内部：调整指针位置，run一下)
    sess.run(init)
    for _ in range(3):
        # 激活函数
        sess.run(update)
        # 激活输出
        print(sess.run(state))

# 占位符（run的时候传入feed_dict）
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
output = tf.multiply(input1, input2)
with tf.Session() as sess:
    print(sess.run(output, feed_dict={input1: [2.], input2: [3.]}))

