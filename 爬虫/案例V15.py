from urllib import request,parse
from http import  cookiejar

# 创建 FileCookieJar 的实例
cookie_name = "cookie.txt"
cookie = cookiejar.MozillaCookieJar(cookie_name)
# 生成 cookie 的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handler = request.HTTPHandler()

# 生成https管理器
https_handler = request.HTTPHandler()

# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)

def login():
    '''
    负责初次登陆
    需要输入用户名密码，用来获取登陆cookie凭证
    :return:
    '''

    # 此url需要从登陆form的action属性中提取
    url = "http://www.renren.com/PLogin.do"

    # 模拟 post 请求
    data = {
        "email":"408629640@qq.com",
        "password":"xixi0909"
    }

    # 把数据进行编码
    data = parse.urlencode(data)

    # 创建一个请求对象
    req = request.Request(url, data=data.encode())

    # 使用 opener 发起请求
    rsp = opener.open(req)

    # 保存cookie文件
    # ignor_discard表示即使cookie将要被丢弃也要保存下来
    # ignor_expire表示如果该文件中cookie即使已经过期，保存
    cookie.save(ignore_discard=True, ignore_expires=True)


if __name__ == '__main__':
    login()
