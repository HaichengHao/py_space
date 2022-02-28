# hello 海程
# 开发时间: 2022/2/28 13:24
# 布尔运算符
# 布尔运算符
# and 、or、 not、 in、 not in
print('--and--')
a,b = 1,2
print(a==1 and b==2)#True    True and True-->True
print(a==1 and b<2) #False    True and False -->False
print(a!=1 and b==2)#False     False and True -->False
print(a!=1 and b!=2) #False False and False -->False

print('--or--')
print(a==1 or b==2) #True or True --> True
print(a!=1 or b==2) #False or True --> True
print(a==1 or b!=2) #True or False --> True
print(a!=1 or b!=2)#False or False --> False

print('--not--  对布尔类型的操作数进行取反')

f1 = True
f2 = False
print(not f1)#not True -->False
print(not f2)#not False -->True

print('--in 与 not in --')
s1='hello world'
print('s'in s1) #False
print('o' in s1) #True
print('w' not in s1) #False 因为w不是不在字符串中
print('k' not in s1)#True 因为k不在字符串中
