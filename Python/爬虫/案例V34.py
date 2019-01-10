from urllib import request
from bs4 import BeautifulSoup

url = "http://www.baidu.com"

rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

# bs自动转码
content = soup.prettify()
#print(content)
print("==" * 30)


print(soup.head)
print("==" * 30)
print(soup.meta)
print("==" * 30)

print("======Tag用法======")
print(soup.link)
print(soup.link.name)
print(soup.link.attrs)  # 字典类型
print(soup.link.attrs['type'])
print("==" * 30)

print("======NavigableString用法======")
print(soup.title)
print(soup.title.name)
print(soup.title.attrs)
print(soup.title.string)
print("==" * 30)

print("======BeautifulSoup用法======")
print(soup.name)
print(soup.attrs)
print("==" * 30)

print("======遍历文档中所有内容======")
for node in soup.head.contents:
    if node.name == "meta":
        print(node)
    if node.name == "title":
        print(node.string)
print("==" * 30)

print("======搜索文档对象======")
tags = soup.find_all(name='meta')
print(tags)
print("======用正则搜索me开头的所有内容======")
import re
tags = soup.find_all(re.compile('^me'), content="always")
for tag in tags:
    print(tag)
print(tags)


