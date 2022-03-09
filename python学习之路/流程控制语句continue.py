# hello 海程
# 开发时间: 2022/3/9 8:39
# continue用于结束当前循环跳到下一个循环
# 要求输出1-50之间所有5的倍数
for i in range (1,51):
    if i%5==0:
        print(i)

# 用continue语句
for i1 in range(1,51):
    if i1%5!=0:
        continue
    print(i1)

# 习题变种 ，打印输出1-50不是5的倍数
for i2 in range(1,51):
    if i2%5!=0 :
        print(i2)

# 用continue语句
for i3 in range(1,51):
    if i3%5==0:
        continue
    print(i3)