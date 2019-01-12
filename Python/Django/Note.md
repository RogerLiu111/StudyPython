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