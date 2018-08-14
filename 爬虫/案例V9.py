'''
访问一个网址
更改自己的UserAgent进行伪装
'''

from urllib import request,error
from io import BytesIO
import gzip

if __name__ == '__main__':

    url = "http://www.baidu.com"

    try:

        # 使用head方法伪装UA
        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1"
        req = request.Request( url, headers=headers)

        # 使用add_header方法
        # req = request.Request(url)
        # req.add_header("User-Agent","Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5")



        # 正常访问
        # 服务器发送给浏览器压缩文件，使用以下方法解压文件才能读取文件。否则压缩过的文件只使用UTF-8解码不了
        rsp = request.urlopen(req)
        html = rsp.read()               # 此处html是压缩过的数据
        buff = BytesIO(html)            # 把html转为文件对象
        f = gzip.GzipFile(fileobj=buff)
        res = f.read().decode()
        print(type(res))
        print(res)

    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)

    print("DONE>...........")