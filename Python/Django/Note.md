# Django系统
- 环境
    - python3.6
    - django1.8
- 参考资料
    - [django中文教程] (https://yiyibooks.cn)
    - django架站的16堂课
# 环境搭建
- anaconda+pycharm
- anaconda使用
    - conda list：显示当前环境安装的包
    - conda env list：显示安装的虚拟环境列表
    - conda create -n env_name python=3.6
    - 激活conda的虚拟环境
        - (Linux)source activate env_name
        - (Windows)activate env_name
    - pip install django=1.8
    
    
# 后台需要的流程

# 创建第一个django程序
- 命令行启动
        
        django -admin startproject DjangoFstTest
        cd DjangoFstTest
        python manage.py runserver
        
- pycharm启动
    - 需要配置
        - File->Settings->project->project interpreter->修改环境(小齿轮点ADD)->Conda Environment->Existing environment->C盘中寻找之前建好的环境(DjangoTest)C:\Users\LALL\AppData\Local\conda\conda\envs\DjangoTest\python.exe
        - Debug manage.py文件，Debug过程中，需要再右上角点进去配置参数，Edit Configurations点进去
           
                Script Path：G:\StudySth\Python\Django\DjangoFstTest\manage.py
                parameters：runserver
                
# 路由系统 -urls
- 创建app
    - app：负责一个具体业务或者一类具体业务的模块
    - python manage.py startapp teacher
    
- 路由
    - 按照具体的请求URL，导入到相应的业务处理模块的一个功能模块
    - django的信息控制中枢
    - 本质上是接受的URL和相应的处理模块的一个映射
    - 在接受URL请求的匹配上使用RE（正则表达式）
    - URL的具体格式入urls.py中所示
- 需要关注两点：
    1.接受的URL是什么，即如何用RE对传入URL进行匹配
    2.已知URL匹配到哪个处理模块
    
- URL匹配规则
    - 从上往下一个一个比对
    - URL格式是分级格式，则按照级别一级一级往下比对，主要应对URL包含子URL的情况
    - 子URL一旦被调用，则不会返回到主URL
        - '/one/two/three/'
    - 正则以r开头，表示不需要转义，注意尖号（^）和美元符号（$）
        - '/one/two/three/'     配对r'^one/'
        - '/oo/one/two/three/'  不配对r'^one/'  
        - '/one/two/three/'     配对r'three/$'
        - '/one/two/three/oo/'     不配对r'three/$'
        - 开头不需要有反斜杠
    - 如果从上向下都没有找到合适的匹配内容，则报错
    
# 正常映射
- 把某一个符合RE的URL映射到事物处理函数中去
    - 举例如下：
        
            from showeast import views as sv
            
            urlpatterns = [
            
                url(r'^admin/', include(admin.site.urls)),
                url(r'^normalmap/', sv.do_normalmap),
           
            ]
# URL中带参数映射
- 在事件处理代码中需要由URL传入参数，形如/myurl/param中的param
- 参数都是字符串形式，如果需要整数等形式需要自行转换
- 通常的形式如下：
    '''
        /seach/page/432     中的432需要经常性的变换，所以我们这里需要带参数的URL
    '''