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
'''
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
'''输出结果为：
hellworld
因为回退了一个格子
'''
# 转义字符格式是在字符前加上'\'
# 原义字符需要在字符串前加上r，例如 print(r"hello\tworld")

#第二章
# 二进制与字符编码
#两个位置可以表示4种状态，8bit=1byte，1024byte=1kb,1024kb=1mb,1024mb=1gb,1024gb=1tb
# 8个位置可以表示256种状态
print(chr(0b100111001011000))



