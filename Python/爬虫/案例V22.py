'''
使用参数headers和params
研究返回结果
'''

import requests

# 完整访问url是下面url加上参数构成
url = "http://www.baidu.com/s?"
search = input("输入你要搜索的内容：")
kw = {
    "wd":search
}

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5702.400 QQBrowser/10.2.1893.400"
}

rsp = requests.get(url, params=kw, headers=headers)
print(rsp.text)
print("*"*30)
print(rsp.content)
print("*"*30)
print(rsp.url)
print("*"*30)
print(rsp.encoding)
print("*"*30)
print(rsp.status_code)  # 请求返回码
print("*"*30)

