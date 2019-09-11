from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt

""" 
    scipy.interpolate 插值是在直线或曲线上的 “两点之间” 找到值的过程

    这种插值工具不仅适用于统计学，而且在科学，商业或需要预测两个现有数据点内的值时也很有用。

    下面的案例，我们使用一组固定的x,y数组，评估出函数模型，并利用该模型计算新的x->y
"""

# 一维插值
x = np.linspace(0, 4, 6)
y = np.cos(x**2/3+4)
f1 = interpolate.interp1d(x, y, kind='linear')  # interp1d ==> 创建基于固定数据点的“函数”。kind 表示插值技术，线性、立方等
f2 = interpolate.interp1d(x, y, kind='cubic')
xnew = np.linspace(0, 4, 30)
plt.plot(x, y, 'o', xnew, f1(xnew), '-', xnew, f2(xnew), '--')  # 根据模型函数，计算x->y，并画图
plt.legend(['data', 'linear', 'cubic'], loc='best')
plt.show()


# 单变量样条曲线
x = np.linspace(-3, 3, 50)
y = np.exp(-x**2) + 0.1 * np.random.randn(50)
f = interpolate.UnivariateSpline(x, y)  # UnivariateSpline ==> 创建基于固定数据点的“函数”。一维平滑样条拟合一组给定的数据点
f.set_smoothing_factor(0.5)  # 设置平滑度 (Must be <= 5. Default is k=3。数值越小，曲线越精确/抖动)
xnew = np.linspace(-3, 3, 1000)
plt.plot(x, y, 'o', xnew, f(xnew), '-')
plt.show()

print('ok')
