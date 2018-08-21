# Python 模块(Module)，是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和Python语句。
# 模块让你能够有逻辑地组织你的 Python 代码段。
# 把相关的代码分配到一个模块里能让你的代码更好用，更易懂。
# 模块能定义函数，类和变量，模块里也能包含可执行的代码。


#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 导入模块
# import support
# support.print_func("Runoob")

# 下面这种调用方式会报错
# import support.print_func
# print_func("Runoob")

# 第二种调用方式
# from support import print_func
# print_func("Runoob")



# 一个模块只会被导入一次，不管你执行了多少次import。这样可以防止导入模块被一遍又一遍地执行。
# Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中

# 这个声明不会把整个 selenium 模块导入到当前的命名空间中，它只会将selenium 里的 webdriver 单个引入到执行这个声明的模块的全局符号表。
from selenium import webdriver
# 一次性引入 math 模块中所有的东西，语句如下
from math import *

#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 导入 package_runoob 包
# from package_runoob.runoob1 import runoob1fun
# from package_runoob.runoob2 import runoob2fun
# runoob1fun()
# runoob2fun()
# -------------------------------------------------------------------------------------------

# from…import *：是把一个模块中所有函数都导入进来; 注：相当于：相当于导入的是一个文件夹中所有文件，所有函数都是绝对路径。
# 使用from…import *导入模块，每次使用模块中的函数，直接使用函数就可以了；注因为已经知道该函数是那个模块中的了
# from  package_runoob.runoob1 import *
# runoob1()


# import 模块：导入一个模块；注：相当于导入的是一个文件夹，是个相对路径。
# import 导入模块，每次使用模块中的函数都要是定是哪个模块

# 像下面引用的话，会报错
# import package_runoob.runoob1
# package_runoob.runoob1fun()
# 这样也会报错
# from package_runoob import runoob1
# runoob1fun()
# 这样也会报错
# from package_runoob import runoob1.runoob1fun
# runoob1fun()

# 像下面引用的话，不会报错
# from package_runoob.runoob1 import runoob1fun
# runoob1fun()
# 像下面引用的话，不会报错
# import package_runoob.runoob1
# package_runoob.runoob1.runoob1fun()
# 像下面引用的话，不会报错
# from package_runoob import runoob1
# runoob1.runoob1fun()