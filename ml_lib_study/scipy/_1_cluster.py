# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from scipy.cluster.vq import kmeans, vq, whiten

""" scipy.cluster 

    scipy实现k-means算法:
    1：根据K个中心将数据集按到中心值距离分簇
    2：将已分的数据集，根据平均向量再确定中心值
    3：重复1、2步骤，直至中心值不再移动（每次的差值与上次相同）
"""


def scatter(data, ax=None, label='data'):
    if not ax:
        # 二维散点图
        plt.scatter(data[:, 0], data[:, 1], label=label)
        plt.legend(loc='upper right')
    else:
        # 三维散点图
        ax.scatter(data[:, 0], data[:, 1], data[:, 2], label=label)
        ax.legend(loc='best')
        ax.set_zlabel('Z', fontdict={'size': 15, 'color': 'red'})
        ax.set_ylabel('Y', fontdict={'size': 15, 'color': 'red'})
        ax.set_xlabel('X', fontdict={'size': 15, 'color': 'red'})


def scatter_cluster(groups):
    # 画出已分类的数据集合a、b、c...的三维散点图（X取每组的第一列，Y取每组的第二列，Z取每组的第三列，每组一个3D图）
    xx = [[] for i in range(len(groups))]
    yy = [[] for i in range(len(groups))]
    zz = [[] for i in range(len(groups))]
    fig = plt.figure()
    ax = Axes3D(fig)
    for i in range(len(groups)):
        for j in range(len(groups[i])):
            xx[i].append(groups[i][j][0])
        for j in range(len(groups[i])):
            yy[i].append(groups[i][j][1])
        for j in range(len(groups[i])):
            zz[i].append(groups[i][j][2])
        scatter(np.vstack((xx[i], yy[i], zz[i])).T, ax=ax, label=i)


def computing_cluster(spott, K):
    # whitening of data（美化数据。缩放数据集的每个特征维度，每个特征除以所有观测值的标准偏差以给出其单位差异。~= 降维）  标准偏差：一种度量数据分布的分散程度之标准，用以衡量数据值偏离 算术平均值 的程度。
    spot = whiten(spott)

    # computing K-Means with K = 3 (3 clusters)
    center, _ = kmeans(spot, K)

    # assign each sample to a cluster （计算上面的概念步骤3，获得最终的分簇）
    cluster, _ = vq(spot, center)

    # Classify data group by cluster
    groups = [[] for i in range(K)]
    for i in range(len(cluster)):
        # 根据聚簇值，选择相应索引的组（cluster元素的值1/2/3，groups元素的索引1/2/3）
        for index in range(len(groups)):
            if cluster[i] == index:
                groups[index].append(spott[i])
    return groups


# 数据准备（三个维度）
spott = np.vstack((np.random.rand(100, 3) + np.array([.5, .5, .5]), np.random.rand(100, 3)))
scatter(spott)
plt.show()

# 计算聚簇，并分类数据
K = 3
groups = computing_cluster(spott, K)

# 画图
scatter_cluster(groups)
plt.show()
