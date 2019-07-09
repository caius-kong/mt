import matplotlib.pyplot as plt
import numpy as np

a = np.random.normal(2, 0.5, 10000)  # 建立一个10000正态偏差的向量，方差为0.5 ^ 2，平均值为2

plt.hist(a, bins=50, density=1)  # 绘制带有50个区间的标准化直方图
plt.show()

# 用numpy计算直方图，然后绘制它
(n, bins) = np.histogram(a, bins=50, normed=True)
plt.plot(.5 * (bins[1:] + bins[:-1]), n)
plt.show()
