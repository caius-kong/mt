import numpy as np

# 二维数组
a = np.arange(15).reshape(3, 5)

print(a)

print(a.sum(), a.max(), a.min())

print(a.sum(axis=0))  # 从x轴看，得到三组数列，求和[x012, x012, x012, x012, x012]

print(a.sum(axis=1))  # 从y轴看，得到五组数列，求和[y01234, y01234, y01234]

print('数据类型:', type(a))

print('维度长度的元组：', a.shape)

print('维度：', a.ndim)

print('元素总数：', a.size)

print('元素数据类型：', a.dtype.name)

print('元素占字节数：', a.itemsize)

# 一维数组
b = np.array([1, 2, 3])
print(b.ndim, "维数组")

# 二维数组
c = np.array([[1, 2, 3], [4, 5, 6]])
print(c.ndim, "维数组")

# 占位型数组
d = np.zeros((3, 4))  # 全0
print(d)

e = np.ones((2, 3, 4), dtype=np.int16)  # 全1， 2叠，3行，4列
print(e)

f = np.empty((2, 3))  # 随机
print(f)

g = np.random.random((2, 3))  # 0-1随机  == np.random.rand(100, 3)
print(g)

# 创建数字序列
h = np.arange(10, 30, 5)
print(h)

i = np.linspace(0, 2, 9)  # 浮点型，linspace更优
print(i)
