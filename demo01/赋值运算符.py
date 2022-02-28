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
