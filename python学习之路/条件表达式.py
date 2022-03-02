# hello 海程
# 开发时间: 2022/3/2 16:47
# 条件表达式
'''题目要求：
从键盘录入两个整数，比较两个整数的大小'''
num1=int(input('请输入第一个整数:'))
num2=int(input('请输入第二个整数:'))
# if num1>=num2:
#     print('num1>=num2')
# else:
#     print('num1<=num2')
'''--结果--
请输入第一个整数:90
请输入第二个整数:700
num1<=num2
'''


print('使用条件表达式进入比较')
print( (str(num1)+'大于等于'+str(num2)) if num1>=num2 else (str(num1)+'小于等于'+str(num2)) )
