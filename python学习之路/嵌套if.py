# hello 海程
# 开发时间: 2022/3/2 16:28
# 嵌套if
# 语法结构：
'''
if 条件表达式1:
    if 内层条件表达式:
        内存条件执行体1
        else:
        内存条件执行体2
    else:
    条件执行体
'''

'''题目：
会员 >=200 ,8折
    >=100 ,9折
      不打折
非会员 >=200 , 9.5折
      不打折'''
answer=input('are you have vip card? y/n')
money=float(input('输入购物金额:'))
if answer=='y':#是会员
    if money>=200:
        print('付款金额为:',money*0.8)
    elif money>=100:
        print('付款金额为:',money*0.9)
    else:
        print('金额未达到打折要求')
elif answer=='n':#不是会员
    if money>=200:
        print('付款金额为:',money*0.95)
    else:
        print('未达到打折要求,不打折')