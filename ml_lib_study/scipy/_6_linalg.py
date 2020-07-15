from scipy import linalg
import numpy as np

"""
    scipy.linalg 线性代数

    包含numpy.linalg，高于numpy.linalg，有很多其他优势，包括编译速度
"""

# 求解线性方程a * x + b * y = 
a = np.array([[1, 3, 5], [2, 5, 1], [2, 3, 8]])
b = np.array([10, 8, 3])
print(linalg.solve(a, b))  # 根据三组方程 x+3y+5z=10, 2x+5y+z=8, 2x+3y+8z=3 --> 求解x,y,z

#