from pandas import DataFrame as df


import re
fn = lambda x: re.match('超时(.*)分钟', x, ).group(1) if re.match('超时(.*)分钟', x, ) else 0
a = df({'key': ['超时21分钟', '超时21分钟', '超时21秒', '']})


a['v'] = a['key'].apply(fn)

print(a)
- run_py:
    - |
        df = to_df(df)
        fn = lambda x: re.match(u'超时(.*)分钟', x, ).group(1) if re.match(u'超时(.*)分钟', x, ) else u'0'
        df[u'超时T分钟'] = df[u'骑手T超时时长'].apply(fn)