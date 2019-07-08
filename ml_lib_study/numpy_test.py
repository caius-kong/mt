import numpy as np

# 多维数组
a = np.arange(8).reshape(3, 5)

print(a)

print('数据类型:', type(a))

print('维度长度元组：', a.shape)

print('维度：', a.ndim)

print('元素总数：', a.size)

print('元素数据类型：', a.dtype.name)

print('元素占字节数：', a.itemsize)

# 一维数组（only）
b = np.array([1, 2, 3])
print(b.ndim)
