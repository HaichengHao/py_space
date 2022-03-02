# hello 海程
# 开发时间: 2022/2/28 8:29
i = 3+4
print(i)
a=b=c=20
print(a,id(a))
print(b,id(b))
print(c,id(c))
print('--支持参数赋值--')
a=20
print(a)
a+=30
print(a)
a-=10
print(a)
a*=30
print(a)
a/=3
print(a)
print(a,type(a))
a//=2
print(a)
print(type(a))
a%=3
print(a)
print('---支持解包赋值---')
a,b,c = 20,30,40
print(a,b,c)

#a,b=20,30,40  将会报错，因为左右变量的个数和值的个数不对应
print('----交换两个变量的值---')
a,b = 10,20
print("交换之前",a,b)
# 交换
a,b = b,a
print("交换之后",a,b)
'''
7
20 1274949469008
20 1274949469008
20 1274949469008
--支持参数赋值--
20
50
40
1200
400.0
400.0 <class 'float'>
200.0
<class 'float'>
2.0
---支持解包赋值---
20 30 40
----交换两个变量的值---
交换之前 10 20
交换之后 20 10

进程已结束，退出代码为 0
'''