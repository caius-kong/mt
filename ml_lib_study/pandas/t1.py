import pandas as pd

from ml_lib_study import res, print_res

df = pd.read_csv('Waves 2019.csv', header=0, encoding='utf-8')  # dataframe【列标签-列名；行标签-索引（0~n）】

df.columns = ['date_time', 'hs', 'hmax', 'tz', 'tp', 'peak_direction', 'sst']  # 重命名列名

res[0] = len(df)

res[1] = df.head(3)

res[2] = df.tail(3)

pd.options.display.float_format = '{:,.2f}'.format  # 将输出限制为2位小数
res[3] = df.describe()  # 生成统计信息（计算25％的数学公式 - min + (max-min) * 百分位数）

print_res()
