# coding=utf-8

from scipy import integrate
from numpy import exp

"""
    scipy.integrate 包提供了许多用于执行 数值积分 的程序
"""


def f(x): return exp(-x**2)


# Quad函数是SciPy积分函数的主力。
# 在a到b给定的固定范围内执行函数f(x)的单个积分的默认选择。
# 四元函数返回两个值，其中第一个数字是积分值，第二个数值是积分值绝对误差的估计值。
print(integrate.quad(f, 0, 1))
