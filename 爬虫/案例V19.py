
'''
破解有道词典
V2
处理JS加密代码
'''
'''
function(e, t) 
{
    var n = e("./jquery-1.7");
    e("./utils");
    e("./md5");
    var r = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10));
    t.recordUpdate = function(e) 
	{
        var t = e.i,
        i = n.md5("fanyideskweb" + t + r + "ebSeFb%=XZ%T[KZ)c(sy!");
        n.ajax(
		{
            type: "POST",
            contentType: "application/x-www-form-urlencoded; charset=UTF-8",
            url: "/bettertranslation",
            data: 
			{
                i: e.i,
                client: "fanyideskweb",
                salt: r,
                sign: i,
                tgt: e.tgt,
                modifiedTgt: e.modifiedTgt,
                from: e.from,
                to: e.to
            },
            success: function(e) {},
            error: function(e) {}
        })
    },后面还有代码...}
'''

'''
通过查找，能找到js代码中操作代码



    
1. 这个就是计算salt公式 salt: r = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10))
2. sign: n.md5("fanyideskweb" + t + r + "ebSeFb%=XZ%T[KZ)c(sy!");
md5一共需要4个参数，第一个和第四个都是固定值的字符串，第三个是所谓的salt，第二个是啥？
第二个参数就是输入的要查找的单词
'''
def getSalt():
    '''
    salt公式是：r = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10))
    把他翻译成Python代码
    :return: 
    '''
    import time, random

    salt = int(time.time()*1000) + random.randint(0,10)

    return salt

def getMD5(v):
    import hashlib
    md5 = hashlib.md5()

    # update需要一个bytes格式的参数
    md5.update(v.encode('utf-8'))
    sign = md5.hexdigest()

    return sign

def getSign(key, salt):
    sign = "fanyideskweb" + key + str(salt) + "ebSeFb%=XZ%T[KZ)c(sy!"
    sign = getMD5(sign)

    return sign

from urllib import request,parse


def youdao(key):

    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    salt = getSalt()

    data = {
        "i":key,
        "from":"AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": str(salt),
        "sign": str(getSign(key, salt)),
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
                "Content-Length":len(data),
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