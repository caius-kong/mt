import numpy as np

a = np.array([[1.0, 2.0], [3.0, 4.0]])

b = np.linalg.inv(a)  # 逆矩阵
print(b)

c = np.eye(4)  # unit 4*4 矩阵
print(c)

d = np.trace(np.arange(16).reshape(4, -1))  # 返回数组对角线的总和(单条)
print(d)