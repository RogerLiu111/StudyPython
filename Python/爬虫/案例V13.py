from urllib import request,parse
from http import  cookiejar

# 创建 cookieJar 的实例
cookie = cookiejar.CookieJar()
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


def getHomePage():

    url = "http://www.renren.com/289451133/profile"

    # 如果已经执行了login函数,则opener自动已经包含了相应的cookie值
    rsp = opener.open(url)

    html = rsp.read().decode()

    with open("rsp13.html","w") as f:
        f.write(html)



if __name__ == '__main__':
    login()
    getHomePage()
