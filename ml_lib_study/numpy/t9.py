# coding=utf-8
import numpy as np

# 多次使用较小的数组来对较大的数组进行算术运算 - 传统做法 - 缺点：当矩阵x非常大的时候，循环任务将会非常缓慢
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x)
for i in range(4):
    y[i, :] = x[i, :] + v
print(y)

# 广播（前提 - 小的数组.shape() = 大数组子元素.shape()） -  其实就是数组计算，只不过扩展到了多维数组与一维数组的计算
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = x + v
print(y)
