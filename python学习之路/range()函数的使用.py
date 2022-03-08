# hello 海程
# 开发时间: 2022/3/8 19:17
# range()函数
# 用于生成一个整数序列
# 创建range()对象的三种方式
# range(stop) -->创建一个[0,stop)之间的整数序列，步长为1
# range(start,stop) -->创建一个[start,stop)之间的整数序列，步长为1
# range(start,top,step) -->创建一个[start,stop)之间的整数序列，步长为step
r = range(10)
print(r)#range(0,10)
print(list(r))#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],默认从0开始，不包含10，默认步长为1

'''第二种方式'''
r1 = range(1,10)
print(list(r1))#[1, 2, 3, 4, 5, 6, 7, 8, 9],给定了start，从1开始，到10结束，不包含10，默认步长为1

'''第三种方式，给了三个参数(小括号里有三个数，start，stop，step)'''
r3=range(1,10,2)
print(list(r3))#[1, 3, 5, 7, 9],从1开始，到10结束，不包含10，步长为2
print(10 in r3)#False，判断序列中的整数
