import pandas as pd
import matplotlib.pyplot as plt

from ml_lib_study import res, print_res

df = pd.read_csv('Waves 2019.csv', header=0, encoding='utf-8')  # dataframe【列标签-列名；行标签-索引（0~n）】

df.columns = ['date_time', 'hs', 'hmax', 'tz', 'tp', 'peak_direction', 'sst']  # 重命名列名

df['month'] = df.date_time.apply(lambda x: pd.to_datetime(x)._short_repr[:7])  # 添加字段

res[0] = df.groupby(df.month).mean()  # 按月分组

# 此时 month 是索引列，无法直接画图，需要 索引-> 列
res[0].reset_index(level=0, inplace=True)  # level=0 指定索引列1，默认全部，    inplace=True 表示修改（不要创建新对象），默认创建新对象

res[0].plot(x='month', y=['hs', 'hmax'])
plt.show()

print_res()

res[0].to_csv('Waves 2019 month.csv')
