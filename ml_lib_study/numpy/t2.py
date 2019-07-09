import numpy as np

# 在数组上的算数运算应用于每个元素
a = np.array([10, 20, 30, 40])
b = np.arange(4)
print(a - b)
print(a * b)  # 注意a*b 与 np.dot(a,b) 不同，前者还是一个数组，后者是向量积，是一个值

# dot 如果处理的是一维数组，则得到的是两数组的內积(点积，向量积)
c = np.arange(0, 9)
d = c[::-1]
print(c)
print(d)
print(np.dot(c, d))

# dot 如果是二维数组（矩阵）之间的运算，则得到的是矩阵积（mastrix product）
e = np.arange(1, 5).reshape(2, 2)
f = np.arange(5, 9).reshape(2, 2)
print(e)
print(f)
print(np.dot(e, f))  # 所得到的数组中的每个元素为，第一个矩阵中与'该元素行号'相同的元素与第二个矩阵与'该元素列号'相同的元素，两两相乘后再求和。例如g1 = (1,2)(5,7), *+

# 小结：向量积可以看做一个特殊的矩阵积，矩阵积 = 多个点的向量积
