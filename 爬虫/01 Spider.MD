# 前提知识
- url
- http协议
- web前端：html，css，js
- ajax
- re，xpath
- xml

# 1.爬虫简介
- 两大特征：
    - 能按作者要求下载数据或者内容
    - 能自动在网络上流窜
- 三大步骤：
    - 下载网页
    - 提取正确的信息
    - 根据一定规则自动跳到另外的网页上执行上两步内容
    
- 爬虫分类
    - 通用爬虫
    - 专用爬虫（聚焦爬虫）
    
- Python网络包简介
    - Python2.x：urllib、urllib2、urllib3、httplib、httplib2、requests
    - Python3.x：urllib、urllib3、httplib2、request
    - Python2：urllib和urllib2配合使用，或者request
    - Python3：urllib和request
    
# 2.urllib
- 包含模块
    - urllib.request：打开和读取urls
    - urllib.error：包含urllib.request产生的常见的错误，使用try捕捉
    - urllib.parse：包含解析url方法
    - urllib.robotparse：解析robots.txt文件
    - 案例V1

- 网页编码问题解决
    - chardet 可以自动检测页面文件的编码格式，但是，可能有误
    - 需要安装：conda install chardet
    - 案例V2
    
- urlopen的返回对象
    - 案例V3
    - geturl：返回请求对象的url
    - info：请求反馈对象的meta信息（源信息）
    - getcode：返回的http code（返回200、403、404、500等状态代码）
    
- request.date的使用
    - 访问网络的两种方法
        - get：
            - 利用参数给服务器传递信息
            - 参数为dict，然后用parse编码
            - 案例V4
        - post：
            - 一般向服务器传递参数使用
            - post是把信息自动加密处理
            - 我们如果想使用post信息，需要用到data参数：
                - Content-Type：application/x-www.form-urlencode
                - Content-Length：数据长度
                - 简而言之，一旦更改请求方法，请注意其他请求头部信息相适应
            - urllib.parse.urlencode可以将字符串自动转换成上面的
            - 案例V5
            - 为了更多的设置请求信息，单纯的通过urlopen函数已经不太够用了
            - 需要利用request.Rquest类
            - 案例V6
           
- urllib.error
    - URLError产生原因：
        - 没网
        - 服务器连接失败
        - 找不到指定服务器
        - 是OSError的一个子类
        - 案例V7
    - HTTPError，是URLError的一个子类
        - 案例V8
        
    - 两者区别：
        - HTTPError是对应的HTTP请求的返回码错误，如果返回错误码是400以上的，则引发HTTPError
        - URLError对应的一般是网络出现问题，包括url问题
        - 隶属关系：OSError->URLError->HTTPError
        
- UserAgent
    - UserAgent：用户代理，简称UA，属于headers的一部分，服务器通过UA来判断访问者身份
    - 常见的UA值，使用的时候可以直接复制粘贴，也可以用浏览器访问的时候抓包
    - 下面是一些常用的UA，也可以直接在浏览器F12，Headers->RequestHeaders中寻找
        1.Android
            Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
        2.Firefox
            Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0 
            Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10
        3.Google Chrome
            Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36 
            Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11 
            Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16
        4.iOS
            Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5
            Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5 
            Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5
        5.QQ浏览器 Android版本 
            MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
            
    - 设置UA可以通过两种方式：
        - heads
        - add_header
        - 案例V9
        
- ProxyHandler处理(代理服务器)
    - 使用代理IP，是爬虫的常用手段
    - 获取代理服务器的地址：
        - www.xicidaili.com
        - www.goubanjia.com
    - 代理用来隐藏真实访问中，代理也不允许频繁访问某一个固定网站，所以，代理一定要很多
    - 基本使用步骤：
        1.设置代理地址
        2.创建ProxyHandler
        3.创建Opener
        4.安装Opener
    - 案例V10

- cookie & session
    - 由于http协议的无记忆性，人们为了弥补这个缺憾，所采用的一个补充协议
    - cookie是发放给用户(即http浏览器)的一段信息，session是保存在服务器上的对应的另一半信息，用来记录用户信息
- cookie和session的区别
    - 存放位置不同
    - cookie不安全
    - session会保存在服务器上一定时间(会有过期时间)
    - 单个cookie保存数据不超过4K，很多浏览器限制一个站点最多保存20个(不属于标准Http协议的内容)
- session的存放位置
    - 存在服务器端
    - 一般情况，session是存放在内存中或者数据库中
    - 没有cookie登陆    案例V11->可以看到，没使用cookie则反馈网页未登陆状态
- 使用cookie登陆
    - 直接把cookie复制下来，然后手动放入请求头   案例V12
    - http模块包含一些关于cookie的模块，通过他们我们可以自动使用cookie
        - CookieJar
            - 管理存储cookie，向传出的http请求添加cookie
            - cookie存储在内存中，CookieJar实例回收后cookie将消失
        - FileCookieJar(filename, delayload=None, policy=None):
            - 使用文件管理cookie
            - filename是保存cookie的文件
        - MozillaCookieJar(filename, delayload=None, policy=None):
            - 创建与Mocilla浏览器(火狐浏览器)cookie.txt兼容的FileCookieJar实例
        - LwpCookieJar(filename, delayload=None, policy=None):
            - 创建与libwww-perl标准兼容的Set-Cookie3格式的FileCookieJar实例
        - 他们的关系是：CookieJar->FileCookieJar->MozillaCookieJar & LwpCookieJar
    - 利用cookieJar访问人人   案例V13
        - 自动使用cookie登陆，大致流程是：
        - 打开登陆页面后自动通过用户名密码登陆
        - 自动提取反馈回来的cookie
        - 利用提取的cookie登陆隐私页面
    - handler是Handler的实例，常用参看案例代码：
        - 用来处理复杂请求

                生成 cookie 的管理器
                cookie_handler = request.HTTPCookieProcessor(cookie)
                创建http请求管理器
                http_handler = request.HTTPHandler()
                生成https管理器
                https_handler = request.HTTPHandler()
    - 创立handler后，使用opener打开，打开后相应的业务有相应的handler处理
    - cookie作为一个变量，打印出来，案例V14
        - cookie的属性
            - name：名称
            - value：值
            - domain：可以访问此cookie的域名
            - path：可以访问此cookie的页面路径
            - expires：过期时间
            - size：大小
            - http字段
    - cookie的保存 - FileCookieJar，案例V15
    - cookie的读取，案例V16

- SSL
    - SSL证书就是指遵守SSL安全套阶层协议的服务器数字证书（SercureSocketLayer）
    - 美国网景公司开发
    - CA（CertifacateAuthority）是数字证书认证中心，是发放，管理，废除数字证书的收信人的第三方机构
    - 遇到不信任的SSL证书，需要单独处理，案例V17
    
- js加密
    - 有的反爬虫策略采用js对需要传输的数据进行加密处理（通常是取md5值）
    - 经过加密，传输的就是密文，但是加密函数或者过程一定是在浏览器完成，也就是一定会把代码（js代码）暴露给使用者
    - 通过阅读加密算法，就可以模拟出加密过程，从而达到破解
    - 过程参看，案例V18,V19
    - 过程比较啰嗦，笔记比较少，需要仔细观察
        - 加密过程一定是在本机完成的，不会把原值发送到服务器在发送回来
        - 知道这个过程以后，查看代码就发现，只有js代码是能够完成加密工作的
        - 查找网站的".js"文件，会发现，代码就在浏览器中，下载下来，仔细观察
        - salt是为了增加密码的复杂度，增加的一个数据，寻找salt，找到加密公式
        - 之后模仿加密过程，求得最后结果
        - 虽然过程复杂，耐心观察与试错，会有结果的！