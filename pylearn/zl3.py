# hello 海程
# 开发时间: 2022/3/22 13:43
from math import *
l1=int(input("请输入第一个边的长度:"))
l2=int(input("请输入第二个边的长度:"))
l3=int(input("请输入第三个边的长度:"))
x=(l1+l2+l3)/2
C=l1+l2+l3
s=x*(x-l1)*(x-l2)*(x-l3)
S=sqrt(s)
print("三角形的周长是:",C)
print("面积为: ",S)