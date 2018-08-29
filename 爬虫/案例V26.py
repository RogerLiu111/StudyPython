'''
search
'''

import re

s = r'\d+'

pattern = re.compile(s)

m = pattern.search("one123324two324three56")
print(m.group())

# 参数表明搜查的起止范围
m = pattern.search("one123324two324three56", 10, 40)
print(m.group())