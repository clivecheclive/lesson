# 列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。
# 列表的数据项不需要具有相同的类型
# 创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。如下所示：

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]

# 使用下标索引来访问列表中的值，同样你也可以使用方括号的形式截取字符
#!/usr/bin/python
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]

print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])



# 可以对列表的数据项进行修改或更新，你也可以使用append()方法来添加列表项，如下所示
list = []          ## 空列表
list.append('Google')   ## 使用 append() 添加元素
list.append('Runoob')
print (list)


# 删除列表项
list1 = ['physics', 'chemistry', 1997, 2000]
list3 = ['physics', 'chemistry', 'adf张三', "李四"]
print(u'{abc}\n'.format(abc='\n'.join(list3)))
print(u'{abc}\n'.format(abc='---------'.join(list3)))

print (list1)
del list1[2]
print ("After deleting value at index 2 : ")
print (list1)

# 列表截取
print (list1[1])
print (list1[-2])#读取列表中倒数第二个元素
print (list1[1:])#从第二个元素开始截取列表

