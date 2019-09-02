# coding=utf-8

from scipy import integrate as inte
from numpy import exp

"""
    scipy.integrate 包提供了许多用于执行 数值积分 的程序
"""


def f(x): return exp(-x**2)


print(inte.quad(f, 0, 1))
