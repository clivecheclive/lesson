# 字典是另一种可变容器模型，且可存储任意类型对象。
# 字典的每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 , 分割，整个字典包括在花括号 {} 中 ,格式如下所示：
# d = {key1 : value1, key2 : value2 }

# 键一般是唯一的，如果重复最后的一个键值对会替换前面的，值不需要唯一。
dict = {'a': 1, 'b': 2, 'b': '3'};
print(dict['b'])
print(dict)

# 元组的值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
dict1 = { 'abc': 456 };
dict2 = { 'abc': 123, 98.6: 37 };
print(dict)
print(dict1)
print(dict2)

# 访问
dict = {'Name': 'Zara', 'Age': 7, 58.9: 'First'};
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
print ("dict['58.9']: ", dict[58.9])

# 向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])
print(dict)

# 删除条目、字典
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
# del dict['Name']; # 删除键是'Name'的条目
# dict.clear();     # 清空词典所有条目
# del dict ;        # 删除词典

print(dict)
print ("dict['Age']: ", dict['Age']);
# print ("dict['School']: ", dict['School']);

# 键必须不可变，所以可以用数字，字符串充当，所以用列表就不行，如下实例：
# cliveche
# dict = {['Name']: 'Zara', 'Age': 7};#会报错
dict3 = {'Name': 'Zara', 'Age': 7};
# dict7 = {dict3: 'Zara', 'Age': 7}
print ("dict['Name']: ", dict3['Name'])

