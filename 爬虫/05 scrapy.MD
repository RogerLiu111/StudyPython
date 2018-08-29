# scrapy
# 爬虫框架
- 框架
- 爬虫框架
    - scrapy
    - pyspider
    - crawley

- scrapy框架介绍
    - 官方文档：https://docs.scrapy.org/en/latest/
    - 中文文档：https://scrapy-chs.readthedocs.io/zh_CN/latest/

- 安装
    - pip install scrapy
    
- scrapy概述
    - 包含各个部件
        - ScrapyEngine：神经中枢，大脑，核心
        - Scheduler调度器：引擎发出来的request请求，调度器需要处理，然后交换引擎
        - Downloader下载器：把引擎发来的request请求，得到response
        - Spider爬虫：负责把下载器得到的网页/结果进行分解，分解成数据+链接
        - ItemPipeline管道：详细处理Item
        - DownloaderMiddleware下载中间件：自定义下载的功能扩展组件
        - SpiderMiddleware爬虫中间件：对spider进行功能扩展
        
- 爬虫项目大概流程
    - 新建项目：scrapy startproject xxx
    - 明确需要目标/产出：编写item.py
    - 制作爬虫：地址 spider/**spider.py
    - 存储内容：pipelines.py
    
- ItemPipline
    - 爬虫提取出数据存入item后，item中保存的数据需要进一步处理，比如清晰，去重，存储等
    - pipeline需要处理process_item函数
        - process_item：
            - 