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
- 'if __name__ == '__main__''的使用
    - 可以有效避免模块代码被导入的时候被动执行的问题
    - 建议所有程序的入口都以此代码为入口
    
# 2.模块的搜索路径和存储
- 什么是模块的搜索路径：
    - 加载模块的时候，系统会在哪些地方寻找此模块
- 系统默认的模块搜索路径
        
        import sys
        sys.path 属性可以获取路径列表
        # print(sys.path)
        # for p in path
            print(p)
            
- 添加搜索路径
        
        path的数据类型是list，给list添加数据使用append扩展。
        sys.path.append(dir) # dir是路径名称
- 模块的加载顺序
    1.在搜索内存中已经加载好的模块
    2.索索Python的内置模块
    3.搜索sys.path路径
    
# 3.包
- 包是一种组织管理代码的方式，里面存放的是模块（类似于文件夹的关系）
- 用于将模块包含在一起的文件夹就是包
- 自定义包的结构

        |---包
        |---|--- __init__.py 包的标志文件     # 有了这个文件,这个文件夹才是包
        |---|--- 模块1                        # .py文件
        |---|--- 模块2      
        |---|--- 子包(子文件夹)               # 嵌套一个包
        |---|--- __init__.py 包的标志文件
        |---|--- 子模块1                        
        |---|--- 子模块2
- 包的导入操作
    - import package_name
        - 直接导入一个包，可以使用__init__.py中的内容
        - 使用方式是:
            
            package_name.func_name
            package_name.class_name.func_name()
    - import package_name as p
        - 具体用法跟作用，与上述取别名的导入一致
        - 注意的是此种方式是默认对__init__.py内容的导入
    - import package.module
        - 导入包中某一个具体的模块
        - 使用方法
            
            package.module.func_name
            package.module.class.fun()
            package.module.class.var
- from ... import 导入
    - from package import module1, module2, ...,
    - 此种导入方法不执行'__init__'的内容
    
            from pkg01 import p01
            p01.sayHello()
    - from package import *
        - 导入当前包'__init__.py'文件中所有的函数和类
        - 使用方法
            
            func_name()
            class_name.func_name()
            class_name.var
            
    - from package.module import *
        - 导入包中指定的模块的所有内容
        - 使用方法
                
            func_name()
            class_name.func_name()
- 在开发环境中经常会引用其他模块，可以在当前包中直接导入其他模块中的内容
    - import 完整的包或者模块的路径
    
- '__all__'的用法
    - 在使用from package import * 的时候，* 可以导入的内容
    - '__init__.py'中如果文件为空，或者没有'__all__'，那么只可以把'__init__.py'中的内容导入
    - '__init__.py'如果设置了'__all__'的值，那么则按照'__all__'指定的子包或者模块进行加载，如此则不会载入'__init__'中的内容
    - '__all__' = ['module1','module2','package1',...]
    
# 命名空间
- 用于区分不同位置不同功能，但相同名称的函数，或者变量的一个特定前缀
- 作用是防止命名冲突

            setName()
            Student.setName()
            Dog.setName()
        - 以上setName所属不同的包，命名空间就是指不同的包