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
        




