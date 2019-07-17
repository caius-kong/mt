import pandas as pd

from ml_lib_study import res, print_res

df = pd.read_csv('Waves 2019.csv', header=0, encoding='utf-8')  # dataframe【列标签-列名；行标签-索引（0~n）】

df.columns = ['date_time', 'hs', 'hmax', 'tz', 'tp', 'peak_direction', 'sst']  # 重命名列名

res[1] = df.head(3).hs  # 指定列(series)，还可以 df.head(3)['hs']  or  df.head(3)[['hs']]

res[2] = df.head(3).hs > 0  # 基于条件生成布尔组(series)

res[3] = df[(df.hs > 0) & (df.hs < 1)].head(3)  # 过滤(df)

res[4] = df[df.date_time.str.startswith('01/01')].head(3)  # 字符串过滤

res[5] = df.iloc[0]  # 获取索引行的series（iloc 数字型，loc 字符型，ix 兼容，字符优先）

print_res()
