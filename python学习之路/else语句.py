# hello 海程
# 开发时间: 2022/3/9 8:51
'''for i in range(3):
    pwd =input('请输入密码:')
    if pwd == '888' :
        print('密码正确')
        break
    else:
        print('密码错误，请重新输入')
else :
    print('已冻结账户')
'''
a=0
while a<3:
    pwd1 = input('请输入密码:')
    if pwd1 =='333':
        break
    else :
        print('请重新输入')
    a+=1
else:
    print('已冻结账户')