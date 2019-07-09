import numpy as np

a = np.arange(15).reshape(3, 5)
print(a)

b = a.ravel()  # 扁平
print(b)

c = a.reshape(5, 3)  # 重构
print(c)

d = a.resize((5, 3))
print(d)

e = c.T  # 颠倒
print(e)

f = np.arange(12).reshape(2, -1)  # -1 表示其他维度自动填充
print(f)

g = np.arange(4).reshape(2, 2)
print(g)
h = np.arange(4, 8).reshape(2, 2)
print(h)

i = np.vstack((g, h))  # 沿着竖直方向将矩阵堆叠起来
print(i)

j = np.hstack((g, h))  # 沿着水平方向将数组堆叠起来
print(j)

k = np.column_stack((g, h))  # 默认hstack，当且仅当一维数组时为vstack
print(k)
