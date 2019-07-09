import numpy as np

# 索引数组索引
a = np.arange(15) ** 2
print(a)

b = np.array([1, 3, 5])
print(a[b])

c = np.array([[1, 3],
              [2, 4]])
print(a[c])

# 当数组 a 是多维的，单个数组指向数组 a 的第一维。（d的第一维就是5个[a,b,c]）
d = np.array([[0, 0, 0],
              [255, 0, 0],
              [0, 255, 0],
              [0, 0, 255],
              [255, 255, 255]])

e = np.array([[0, 1, 2, 0],
              [0, 3, 4, 0]])
print(d[e])

f = np.arange(12).reshape(3, 4)
g = np.array([[0, 1],
              [1, 2]])
h = np.array([[2, 1],
              [3, 3]])
print(f[g, h])  # 先计算g，取f的第一维度，再计算h，取之前结果的每行的列索引值

# argmax 返回沿轴axis最大值的索引
i = np.array([[0, 1, 2],
              [3, 4, 5]])
print(np.argmax(i))  # 未指定axis，扁平化后取
print(np.argmax(i, axis=0))  # x轴（列），2*[a,b,c]，即求列最大值的索引，即[1,1,1]
print(np.argmax(i, axis=1))

# 布尔数组索引
j = np.arange(12).reshape(3, 4)
k = j > 4
print(k)
print(j[k])  # 打印True的
j[k] = 0  # True的赋值0
print(j)
