# hello 海程
# 开发时间: 2022/3/2 15:54
# 选择结构
money=1000 #余额
s=int(input('输入取款金额')) #取款金额
# 判断余额是否充足
if money>=s :
    money=money-s
    print('取款成功，余额为:',money)
else: print('余额不足，余额为:',money)