# 动态HTML

## 爬虫跟反爬虫

## 动态HTML介绍
- JavaScrapt
- jQuery
- Ajax
- DHTML

- Python采集动态数据
    - 从JavaScript代码入手采集
    - Python第三方库运行JavaScript，直接采集你在浏览器看到的页面
    
## Selenium + PhantomJS
- Selenium：web自动化测试工具
    - 自动加载页面
    - 获取数据
    - 截屏
    - 安装：pip install selenium==2.48
    - 官网：http://selenium-python.readthedocs.io/index.html
- PhantomJS(幽灵浏览器)
    - 基于webkit的无界面的浏览器
    - 官网：http://phantomjs.org/download.html
- Selenium库有一个WebDriver的API
- WebDriver可以跟页面上的元素进行各种交互，用他可以来进行爬取
- 案例V36

- chrome + chromedriver
    - 下载安装chrome：下载 + 安装
    - 下载安装chromedriver：
- Selenium操作主要分两大类：
    - 得到UI元素
        - find_element_by_id
        - find_elements_by_name
        - find_elements_by_xpath
        - find_elements_by_link_text
        - find_elements_by_partial_link_etxt
        - find_elements_by_tag_name
        - find_elements_by_class_name
        - find_elements_by_css_selector
    - 基于UI元素操作模拟
        - 单击
        - 右击
        - 拖拽
        - 输入
        - 可以通过导入ActionsChains类来做到
        - 案例V37