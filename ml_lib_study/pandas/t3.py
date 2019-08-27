import pandas as pd

from ml_lib_study import res, print_res

df = pd.read_csv('Waves 2019.csv', header=0, encoding='utf-8')  # dataframe【列标签-列名；行标签-索引（0~n）】

df.columns = ['date_time', 'hs', 'hmax', 'tz', 'tp', 'peak_direction', 'sst']  # 重命名列名

df = df.set_index(['date_time'])  # 自定义索引(列 ——> 索引)，默认索引是0~n
res[1] = df.head(3)

# res[2] = df.loc('01/01/2017 01:00')

res[3] = df.sort_index(ascending=False).head(3)  # 按索引排序(降序)

df = df.reset_index('date_time')  # 撤销指定索引
res[4] = df.head(3)

print_res()
