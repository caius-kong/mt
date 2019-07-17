import pandas as pd

from ml_lib_study import res, print_res

df = pd.read_csv('Waves 2019.csv', header=0, encoding='utf-8')  # dataframe【列标签-列名；行标签-索引（0~n）】

df.columns = ['date_time', 'hs', 'hmax', 'tz', 'tp', 'peak_direction', 'sst']  # 重命名列名

df['year'] = df.date_time.apply(lambda x: pd.to_datetime(x).year)  # 应用函数，基于一列数据，生成另一列数据
res[0] = df.head(3)

res[1] = df.groupby(df.year).mean()  # 分组，计算

res[2] = df.groupby([df.year, df.hs.astype(int)])[['hmax', 'tz', 'tp', 'peak_direction', 'sst']].mean()  # 组合分组

res[3] = res[2].unstack(0)  # 将一列数据设置为列标签

# res[4] = df.pivot('year', 'hs')[['hmax', 'tz', 'tp', 'peak_direction', 'sst']].fillna('')

df1 = pd.DataFrame({'year': [2017, 2018, 2019], 'data1': range(3)})
df2 = pd.DataFrame({'year': [2017, 2018, 2019], 'data2': range(3)})
res[5] = df1.merge(df2)  # 合并数据集（会自动根据相同的列名合并）

print_res()
