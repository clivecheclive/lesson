
#!/usr/bin/python
#  -*- coding: UTF-8 -*-
num = 5
if num == 3:            # 判断num的值
    print('boss')
elif num == 2:
    print('user')
elif num == 1:
    print('worker')
elif num < 0:           # 值小于零时输出
    print('error')
else:
    print('roadman')    # 条件均不成立时输出




#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 例3：if语句多个条件

num = 9
if num >= 0 and num <= 10:    # 判断值是否在0~10之间
    print('hello')
# 输出结果: hello

num = 10
if num < 0 or num > 10:    # 判断值是否在小于0或大于10
    print('hello')
else:
    print('undefine')
# 输出结果: undefine

num = 8
# 判断值是否在0~5或者10~15之间
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
    print('hello')
else:
    print('undefine')
# 输出结果: undefine