import numpy as np

a = np.array([[1, 2], [3, 4]])
sum0 = np.sum(a, axis=0)
sum1 = np.sum(a, axis=1)
print(sum0)  # 沿着0/x轴看，是[1,2]，[3,4]两个向量，即列求和，[4 6]
print(sum1)  # 沿着1/y轴看，是[1,3]，[2,4]两个向量，即行求和，[3 7]
