import numpy as np

a = np.arange(12)

b = a  # 同一个对象的两个名称
print(b is a)

# 数组拷贝 - 浅拷贝 - 新对象新数据（仅对象的内存点不一致）
c = a.view()
print(c is a)
print(c.base is a)
a.shape = 3, 4
c.shape = 2, 6  # a's shape doesn't change
print(a)
print(c)

c[0, 4] = 1234  # a's data changes（混淆点）
print(a)

s = a[:, 1:3]
s[:] = 10  # s[:] is a view of s，so a's data changes
print(a)

# 数组拷贝 - 深拷贝 - 新对象新数据（对象、数据内存点都不一致）
d = a.copy()
print(d is a)
print(d.base is a)
d[0, 0] = 9999
print(a)
