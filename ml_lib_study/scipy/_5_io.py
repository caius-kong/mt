import scipy.io as sio
import numpy as np

"""
    scipy.io 提供了多种功能来解决不同格式的文件(输入和输出)

    其中一些格式是:
        Matlab
        IDL
        Matrix Market
        Wave
        Arff
        Netcdf
        ...

    接口：
        savexx()
        loadxx()
        whoxx()
"""

# example .mat file (一种二进制文件)
vect = np.arange(10)
sio.savemat('array.mat', {'vect':vect})

content = sio.loadmat('array.mat')
print(content)

content = sio.whosmat('array.mat')  # 和loadmat的区别，此函数不读取数据到内存，仅检查文件内容
print(content)

print('ok')


