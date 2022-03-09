# hello 海程
# 开发时间: 2022/3/9 7:58
# for in 循环
for item in 'python' : #第一次取出来的是p,将p赋值item,将item的值取出
    print(item)


# range()产生一个整数序列，也是一个可迭代对象
for i in range(10):
    print(i)
# 如果在循环中不需要使用自定义变量，可将自变量写为“_”
for _ in range(5):
    print('hello')


print('1-100偶数累加和')
sum = 0
for e in range(1,101):
    if e%2==0 :
        sum+=e
print('1到100的偶数累加和为:',sum)