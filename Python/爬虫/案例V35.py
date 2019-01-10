
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
titles = soup.select("title")
print(titles[0])
print("==" * 30)
metas = soup.select("meta[content='always']")
print(metas)
print("==" * 30)
print("==" * 30)
print("==" * 30)
print("==" * 30)

