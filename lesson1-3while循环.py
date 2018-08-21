#!/usr/bin/python

count = 0
while (count < 9):
   print('The count is:',count)
   count = count + 1

print("Good bye!")


# continue 和 break 用法
i = 1
while i < 10:
    i += 1
    if i%2 > 0:     # 非双数时跳过输出
        continue
    print (i)         # 输出双数2、4、6、8、10

i = 1
while 1:            # 循环条件为1必定成立
    print (i)         # 输出1~10
    i += 1
    if i > 10:     # 当i大于10时跳出循环
        break




count = 0
while count < 5:
   print(count, " is  less than 5")
   count = count + 1
else:
   print(count, " is not less than 5")




#类似 if 语句的语法，如果你的 while 循环体中只有一条语句，你可以将该语句与while写在同一行中， 如下所示
flag = 0
while (flag): print('Given flag is really true!')

print("Good bye!")


