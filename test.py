from pandas import DataFrame as df
import re


# fn = lambda x: re.match('超时(.*)分钟', x, ).group(1) if re.match('超时(.*)分钟', x, ) else 0
fn = lambda x: u'%s' % (int(re.match(u'(.*)小时(.*)分钟', x, ).group(1)) * 60 + int(
    re.match(u'(.*)小时(.*)分钟', x, ).group(2))) if re.match(u'(.*)小时(.*)分钟', x, ) else u'0'

a = df({'key': ['21小时13分钟', '0小时13分钟', '10小时0分钟', '']})


a['v'] = a['key'].apply(fn)

print(a)
