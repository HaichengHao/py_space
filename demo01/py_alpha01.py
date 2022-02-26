# hello 海程
# 开发时间: 2022/2/17 16:03
##python中的输出函数
  #print()
  #可以输出数字和字符串以及含有运算符的表达式
print(520)
print('hello world') #字符串需要加引号
print(3+1)

# 将数据输出文件中
'''
fp=open('D:/py_space/pytest.txt','a+')
print('hello',file =fp)
fp.close()
'''
# 不换行输出
print('hello','world','python')

#转义字符
# 换行 \n
# 回车 \r
# 水平制表 \t
#
print("hello\nworld")
print("hello\tworld")
print("helloooo\tworld")
''' --结果--
hello	world
helloooo	world
/t会生成四个制表位，不够则开辟
'''
print('hello\rworld')
'''
输出结果为：
world
\r会回退\r之前的内容，所以只有一个world
'''
print('hello\bworld')
'''---结果---
hellworld
因为回退了一个格子
'''
# 转义字符格式是在字符前加上'\'
# 原义字符需要在字符串前加上r，例如 print(r"hello\tworld")
#
# 第二章
# 二进制与字符编码
# 两个位置可以表示4种状态，8bit=1byte，1024byte=1kb,1024kb=1mb,1024mb=1gb,1024gb=1tb
# 8个位置可以表示256种状态
print(chr(0b100111001011000))

# 变量的定义和使用
# name ='mariya'
# print(name)
# print('标识，也就是内存地址',id(name))
# print('类型',type(name))
# print('值',name)
'''
---结果---
mariya
标识，也就是内存地址 1574648175792
类型 <class 'str'>
值 mariya
'''
name='mariya'
print(id(name))
name='wawa'
print(name)
print(id(name))
'''---结果---
 1739532426416
 wawa
 1739532426352
'''


# 数据类型
# 整数类型(integer) 浮点型(float) 字符型(string)
n1 = 90
n2 = -76
n3 = 0
print(n1)
print(n2)
print(n3)
print(n1,type(n1))
print(n2,type(n2))
print(n3,type(n3))
'''---结果---
90
-76
0
90 <class 'int'>
-76 <class 'int'>
0 <class 'int'>
'''
# 浮点数相加
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))
#布尔类型(boolen)
'''可以用0或1来表示 
   0代表False 
   1代表True'''

# 字符串类型(string)
# 不可变的字符序列
str1 = "life is short ,you need python"
print(str1,type(str1))
str2 = 'life is short ,you need python'
print(str2,type(str2))
str3 = '''life is short , 
you need python '''
print(str3,type(str3))
str4 = """life is short,
you need python"""
print(str4,type(str4))


