'''
破解有道词典
V1
'''

from urllib import request,parse


def youdao(key):

    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    data = {
        "i":"gile",
        "from":"AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "1534840967561",
        "sign": "6e83aa388d61de77fe76d9fc2f23d624",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false"
    }

    # 参数data需要时bytes格式
    data = parse.urlencode(data).encode()

    headers = {
                "Accept":"application/json,text/javascript,*/*;q=0.01",
                #"Accept-Encoding":"gzip,deflate",
                "Accept-Language":"zh-CN,zh;q=0.9",
                "Connection":"keep-alive",
                "Content-Length":"200",
                "Content - Type":"application/x-www-form-urlencoded; charset=UTF-8",
                "Cookie":"OUTFOX_SEARCH_USER_ID=-907020126@10.169.0.83; JSESSIONID=aaarLem5ijg_AeWxNPBvw; OUTFOX_SEARCH_USER_ID_NCOO=2053074192.560825; ___rl__test__cookies=1534840967505",
                "Host":"fanyi.youdao.com",
                "Origin":"http://fanyi.youdao.com",
                "Referer":"http://fanyi.youdao.com/",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5702.400 QQBrowser/10.2.1893.400",
                "X-Requested-With":"XMLHttpRequest"
    }

    req = request.Request(url=url, data=data, headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()

    print(html)

if __name__ == '__main__':
    youdao("girl")