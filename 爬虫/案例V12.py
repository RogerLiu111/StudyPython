

from urllib import request
import chardet

if __name__ == "__main__":

    url = "http://www.renren.com/910258352"

    headers = {
        "Cookie":"anonymid=jkwa8m22hzpexj; depovince=GW; _r01_=1; JSESSIONID=abcd2vdh6uWJN9CUUXbvw; __guid=238633222.1751689399254483000.1534406885913.0918; ick_login=fd5edd40-ff0a-4b0f-9659-183e1bf27069; t=3b7349f5cba3388cb498ffcf74f906742; societyguester=3b7349f5cba3388cb498ffcf74f906742; id=910258352; xnsid=be38b656; jebecookies=0b3d4492-cf73-41c8-83b5-72b128068acb|||||; ver=7.0; loginfrom=null; monitor_count=2; jebe_key=90c44a0c-576b-4139-80d0-ce0ab58d8354%7Cb28ef9280d3f362813ecfdb3297c0910%7C1534406906674%7C1%7C1534406912139; wp_fold=0"
    }

    req = request.Request(url, headers=headers)

    rsp = request.urlopen(req)



    html = rsp.read()
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)
    html = html.decode(cs.get("encoding","utf-8"))
    # 保存文件
    with open("rspV12.html","w") as f:
        f.write(html)