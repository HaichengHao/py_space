# hello 海程
# 开发时间: 2022/2/28 8:53
# 比较运算符，对变量或表达式的结果进行大小，真假等比较
print('对变量或表达式的结果进行大小，真假等比较')
# >,<,>=,<=,!=
# == 对赋值对象进行比较
# is , is not 对象id的比较

a,b = 10, 20
print('a>b',a>b)
# 结果为：a>b False

# 比较运算符的结果为布尔类型
print('a<b',a<b)
# 结果：a<b True
print('a不等于b',a!=b)
# 结果：a不等于b True

"一个= 称为赋值运算符，而 == 为比较运算符" \
"一个变量由三部分组成，标识，类型，值" \
"== 比较的是值还是标识呢？"

"答案，比较的是值"

"比较对象的标识用的是 is"

a=10
b=10
print(a == b)#True,说明a与b的值相等
print(a is b)#True，说明a与b的id标识相等

print(id(a))#1511372292624
print(id(b))#1511372292624
# 可以发现a与b的存储的标识一样

# 以下代码暂未学习
lst1 = [11,22,33,44]
lst2 = [11,22,33,44]
print(lst1 == lst2) #True
print(lst1 is lst2) #False
print(id(lst1))#1411115667456
print(id(lst2))#1411116028352
print(a is b) #True
print(a is not b) #False ,因为a,b的id是相等的
print( lst1 is not lst2) #True
#可以发现lst1 和 lst2的值相等，但id并不相等
