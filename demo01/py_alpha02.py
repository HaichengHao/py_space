# hello 海程
# 开发时间: 2022/2/23 14:57
# 数据类型转换
name = '张三'
age =20
print(type(name),type(age))
# print('我叫'+name+'今年'+age+'岁了')#报错
print('我叫'+name+'今年'+str(age)+'岁了')#做类型转换之后就会正常输出
'''--结果--
D:\python\python.exe D:/py_space/demo01/py_alpha02.py
<class 'str'> <class 'int'>
我叫张三今年20岁了
'''
# 将其他类型转换为str类型时需要str()
a=10
print(str(a),type(str(a)))
'''---结果---
10 <class 'str'>
'''
# 转换为int类型，int()
# 将str类型转换为整数类型时，只能转换整数类型的数字串，如'123',但是’123.4‘是不可以转换的
s1='124'
print(type(s1))
f1=98.2
print(type(f1))
print(int(s1),type(int(s1)))
print(int(f1),type(int(f1)))
'''--结果--
124 <class 'int'>
98 <class 'int'>
'''