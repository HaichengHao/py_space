# hello 海程
# 开发时间: 2022/3/2 16:05
# 多分支结构
'''多分支结构，多选一执行，从键盘录入一个整数，成绩
90-100 A
80-89 B
70-79 C
60-69 D
0-59 E
小于0或大于100为非法数据
'''
score=int(input('输入成绩:'))
if score>=90 and score<=100:
    print('A级')
elif score>=80 and score<=89:
    print('B级')
elif score>=70 and score<=79:
    print('C级')
elif score>=60 and score<=69:
    print('D级')
elif score>100 or score<0:
    print('成绩输入错误，请重新输入')
