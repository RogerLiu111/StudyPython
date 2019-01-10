'''
Python中正则模块是re
使用大致步骤：
1.compile函数将正则表达式的字符串编译为一个Pattern对象
2.通过Pattern对象的一系列方法对文本进行匹配，匹配结果是一个Match对象
3.用Match对象的方法，对结果进行操纵
'''

import re

# \d表示一个数字
# 后面+号表示这个数字可以出现一次或多次
s = r"\d+" # r表示后面是原生字符串，后面不需要转义

# 返回Pattern对象
pattern = re.compile(s)
# 返回一个match对象
# 默认找到一个匹配对象就返回
m = pattern.match("one12two2three3")
print(type(m))
# 匹配默认是从头开始查找，所以此次结果为None
print(m)

# 返回一个match对象
# 后面为位置参数，含义是从哪个位置开始查找，找到哪个位置结束
m = pattern.match("one1246.464two2three3", 3, 10)
print(type(m))
print(m)
print(m.group())    # 打印出查找到的内容
print(m.start(0))   # 查找到的内容的起始位置
print(m.end(0))     # 查找到的内容的结束位置
print(m.span(0))    # 查找到的内容的位置区间