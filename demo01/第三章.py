# hello 海程
# 开发时间: 2022/2/26 21:49
# 第三章课程介绍
# 1.python中的输入函数input()
# 2.python中的运算符
# （1）算术运算符
# （2）赋值运算符
# （3）比较运算符
# （4）布尔运算符
# （5）位运算符
# 3.运算符的优先级


# input函数的使用
# 例子：
'''
present = input("小鬼想要什么礼物呢？")
print(present,type(present))'''
# 练习题，计算两个输入整数的和
'''
a = int(input("请输入第一个加数"))
b = int(input("请输入第二个加数"))
print("它们的和为：",a+b)'''
'''---结果---
D:\python\python.exe D:/py_space/demo01/第三章.py
请输入第一个加数5
请输入第二个加数4
它们的和为： 9'''
# python中常用的运算符
# 标准算数运算符
# 例子
print(1+1) #执行加法运算
print(1-1) #减法运算
print(1*1) #乘法运算
print(1/2)#除法运算
print(11//2)#整除运算
print(11%2)#取余运算
print(2**3)#幂运算 //2的3次方
'''--结果--
2
0
1
0.5
5
1
8'''

#*一正一负的整除和取余运算
print(9//4)
print(-9//-4)
print(-9//4) #一正一负向下取整
print(9%-4)#余数=被除数-除数*商 9-（-4）*（-3）
print(-9%4)#-9-4*（-3）=-->3

'''--结果--
2
2
-3
-3
3'''

