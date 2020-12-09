from pandas import DataFrame as df
import re


# fn = lambda x: re.match('超时(.*)分钟', x, ).group(1) if re.match('超时(.*)分钟', x, ) else 0
fn = lambda x: 1 if '分钟' in x else 0
a = df({'key': ['2.12 元', '0小时13分钟', '10小时0分钟', '']})


a['v'] = a['key'].apply(fn)

print(a)
