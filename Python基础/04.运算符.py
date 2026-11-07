# print("10+4=",10+4)
# print("10*4=",10*4)
# print("10/4=",10/4)
# print("10//4=",10//4)
# print("10%4=",10%4)
# print("10**4",10**4)
#
# #算术运算符的优先级---**-->* / //-->+ -
# print("0.1 + 10 / 4 ** 2=",0.1+10/4**2)
from operator import and_

#案例
# print("分别设两个数为x,y")
# x = input("x=")
# y = input("y=")
# print("x=",float(x),"y=",float(y))
# print(f"x+Y=",float(x)+float(y))
# print(f"x+Y=",float(x)-float(y))
#0.999999999 --->精度损失，由于计算机基于二进制进行数据的运算与处理，所以无法精确的表示所有的小数，涉及到浮点数的运算会产生误差

#赋值运算符
# num = 85
#
# num += 10
# print("num += 10后,num=",num)
# num -= 10
# print("num -= 10后,num=",num)
# num *= 10
# print("num *= 10,num=",num)
# num /= 10
# print("num /= 10,num=",num)
# num %= 10
# print("num %= 10,num=",num)
# num **= 10
# print("num **= 10,num=",num)

#逻辑运算符
#键盘录入一个整数，判断它是否在10--20之间
num = float(input("请输入一个数字:"))
print(f"num在10到20之间:", 10<=num<=20)
num = float(input("请输入一个数字:"))
print(f"num不在10到20之间",not 10<=num<=20)
print(f"num在10到20之间",10>num or 10>20)


