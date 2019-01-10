'''
利用request下载页面
自动检测页面编码

'''

import urllib


if __name__ == '__main__':
    url = 'http://finance.eastmoney.com/news/1345,20180813925127596.html'

    rsp = urllib.request.urlopen(url)

    print(type(rsp))
    print(rsp)

    print("url：{0}".format(rsp.geturl()))
    print("*"*30)
    print("Info：{0}".format(rsp.info()))
    print("*"*30)
    print("Code：{0}".format(rsp.getcode()))
    html = rsp.read()

    html = html.decode()
    #print(html)