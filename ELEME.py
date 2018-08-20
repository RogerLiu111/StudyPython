'''
爬取饿了么账户内的信息：
1.每日单量信息
2.每日竞价使用情况

'''

from urllib import request,parse
from http import cookiejar

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
    url = "https://melody.shop.ele.me/login"

    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1"

    # 模拟 post 请求
    # data = {
    #     "id":"654241d0-9adb-4e0b-9ff2-a24568a9a1cb",
    #     "metas":{appName: "melody", appVersion: "4.4.0"},
    #     "method":"loginByUsername",
    #     "ncp":"2.0.0",
    #     "params":{username: "chaofun222", password: "chaofun222", captchaCode: "", loginedSessionIds: []},
    #     "service":"LoginService"
    # }

    # data = {
    #     "id":"654241d0-9adb-4e0b-9ff2-a24568a9a1cb",
    #     # "metas":{appName: "melody", appVersion: "4.4.0"},
    #     "appName": "melody",
    #     "appVersion": "4.4.0",
    #     "method":"loginByUsername",
    #     "ncp":"2.0.0",
    #     # "params":{username: "chaofun222", password: "chaofun222", captchaCode: "", loginedSessionIds: []},
    #     "username":"chaofun222",
    #     "password":"chaofun222",
    #     "captchaCode":"",
    #     "loginedSessionIds" :[],
    #     "service":"LoginService"
    # }

    metas ={
        "appName":"melody",
        "appVersion": "4.4.0"
    }
    params = {
        "username": "chaofun222",
        "password": "chaofun222",
        "captchaCode": "",
        "loginedSessionIds": []
    }
    data = {
        "id":"654241d0-9adb-4e0b-9ff2-a24568a9a1cb",
        "metas":metas,
        "method":"loginByUsername",
        "ncp":"2.0.0",
        "params":params,
        "service":"LoginService"
    }

    # 把数据进行编码
    data = parse.urlencode(data)

    # 创建一个请求对象
    req = request.Request(url, data=data.encode(), headers=headers)

    # 使用 opener 发起请求
    rsp = opener.open(req)

def get_JSJLD_Page():

    url_dashboard = "https://melody.shop.ele.me/app/shop/2320841/dashboard"
    # 如果已经执行了login函数,则opener自动已经包含了相应的cookie值
    rsp_dashboard = opener.open(url_dashboard)
    html_dashboard = rsp_dashboard.read().decode()
    with open("jsjld.html","w") as f:
        f.write(html_dashboard)

    '''
    url_vas = "https://melody.shop.ele.me/app/shop/2320841/vas"
    rsp = opener.open(url)
    html = rsp.read().decode()
    with open("rsp13.html","w") as f:
        f.write(html)
    '''

if __name__ == '__main__':
    '''
    执行完login之后，会得到授权之后的cookie
    我们尝试把cookie打印出来
    '''
    login()
    #get_JSJLD_Page()
