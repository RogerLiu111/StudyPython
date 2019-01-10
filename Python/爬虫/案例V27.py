'''
findall案例
'''

import re

pattern = re.compile(r'\d+')

s = pattern.findall("i sf 35 dg435 fgfh5545  4543 546")

print(s)

pattern = re.compile(r'\d+')

s = pattern.finditer("i sf 35 dg435 fgfh5545  4543 546")
print(type(s))
for i in s:
    print(i)            # i返回的是一个match类型，group之后直接出结果
    print(i.group())