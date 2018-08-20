'''

'''

from urllib import request

if __name__ == "__main__":

    url = "http://www.renren.com/910258352"

    rsp = request.urlopen(url)
    html = rsp.read().decode('utf-8')

    # 保存文件
    with open("rsp.html","w") as f:
        f.write(html)