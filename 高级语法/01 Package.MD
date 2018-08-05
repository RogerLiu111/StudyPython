# 1.模块
- 如何使用模块
    - 模块直接导入
        - 加入模块名称以数字开头，需要借助importlib帮助
    - 语法
    
            import module_name
            module_name.function_name
            module_name.class_name
    - 导入的同时给模块起一个别名
    - 其余用法跟第一种相同
    
            import 模块 as 别名
            
    - 按下列方法有选择性的导入
    - 使用的时候可以直接使用导入的内容,不需要前缀 
    
            from module_name import func_name, class_name
    - 导入模块所有内容
    
            from module_name import *
            