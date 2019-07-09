import numpy as np

a = np.fromfunction(lambda x, y: x * 10 + y, (5, 4), dtype=int)  # 5行4列矩阵，每个元素 = row_num*10 + col_num
print(a)

b = a[:, 1]  # 行切片，取每行的第2列
print(b)

c = a[1:3, :]  # 列切片，取每列的第2，3行
print(c)

d = a[2, 3]  # 取指定索引元素
print(d)

e = a[1]  # 索引不全，按全切片处理，列切片取行值
print(e)

f = np.array([[[0, 1, 2],
               [10, 12, 13]],
              [[100, 101, 102],
               [110, 112, 113]]])
g = f[1]  # 全切片，取第一叠，same as f[1,:,:] or f[1, ...]
print(g)

# 遍历axis=0
for x in a:
    print(x)

# 遍历每个元素
for x in a.flat:
    print(x)
