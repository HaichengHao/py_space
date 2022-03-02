# hello 海程
# 开发时间: 2022/3/2 15:27
# 对象的布尔值
# python中一切皆是对象，所有对象都有一个布尔值
# 获得对象的布尔值 使用内置函数bool()
# 以下对象的布尔值皆为false
'''
False
数值0
None
空字符串
空列表
空元组
空字典
空集合
'''

# 测试对象的布尔值
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(''))
print(bool(""))
print(bool([]))#空列表
print(bool(list()))#空列表
print(bool({}))#空字典
print(bool(dict()))#kon字典
print(bool(tuple()))#空元组
print(bool(set()))#空集合

print("--结果皆是False--")