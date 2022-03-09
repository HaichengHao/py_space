# hello 海程
# 开发时间: 2022/3/9 8:29
# 流程控制语句break
# 用于结束循环结构，通常与分支结构if使用
'''从键盘录入密码，最多录入三次，如果正确就结束循环'''
for i in range(3):
    pwd =input('请输入密码:')
    if pwd == '888' :
        print('密码正确')
        break
    else:
        print('密码错误，请重新输入')
