# score = 700
# if score > 680:
#     print("恭喜你被清华录取了")
# print("--------------------")

# #案例
# ok_zhang_hao = "188888888888"
# ok_mi_ma = "666888"
# zhang_hao = input("请输入您的帐号:")
# mi_ma = input("请输入您的密码:")
# if zhang_hao == ok_zhang_hao and mi_ma == ok_mi_ma:
#     print("登陆成功")
# if zhang_hao != ok_zhang_hao and zhang_hao != ok_mi_ma:
#     print("账号或密码错误，登陆失败")

# #案例 if...else...
# ok_zhang_hao = "188888888888"
# ok_mi_ma = "666888"
# zhang_hao = input("请输入您的帐号:")
# mi_ma = input("请输入您的密码:")
# if zhang_hao == ok_zhang_hao and mi_ma == ok_mi_ma:
#     print("登陆成功")
# else:
#     print("账号或密码错误，登陆失败")

#案例 根据用户输入的年份判断其是否为闰年，如为非整年能整除四为闰年，若为整数年能整除四百为闰年
# year = int(input("请输入年份:"))
# if (year % 4 == 0 and year % 100 !=0 ) or (year %400 == 0):
#     print("该年份为闰年")
# else:
#     print("该年份不是闰年")

#练习
#1 根据用户输入的数字，判断奇偶
# num = int(input("请输入数字:"))
# # if num % 2 == 0 :
# #     print(f"{num}是偶数")
# # else:
# #     print(f"{num}是奇数")
# #根据年龄判断用户是否成年
# # year = int(input("请输入您的年龄:"))
# # if year >= 18:
# #     print("您已成年")
# # else:
# #     print("您未成年")
#
# #if elif else
# # num = int(input("请输入一个数字:"))
# # if num > 0:
# #     print("该数字为正数")
# # elif num < 0:
# #     print("改数字为负数")
# # else:
# #     print("改数字为0")
#
# #根据用户输入的用户名和密码进行系统登录
# user_name = input("请输入用户名:")
# password = input("请输入密码:")
# if user_name == "admin" and password == "666888":
#     print("登录成功")
# elif user_name == "root" and password == "547527":
#     print("登陆成功")
# elif user_name == "zhangsan" and password == "123456":
#     print("登陆成功")
# else:
#      print("账号或密码错误,登陆失败")
#  #根据输入的三个边长（正整数）判断等腰三角形，等边三角形，普通三角形，亦或是无法构成三角形
# a = int(input("a的边长为:"))
# b = int(input("b的边长为:"))
# c = int(input("c的边长为:"))
# if a+b>c and a+c>b and b+c>a:
#     print("三边能构成三角形")
#     if a == b == c:
#         print("该三角形为等边三角形")
#     elif a == b and b != c:
#         print("三角形为等腰三角形")
#     elif a == c and c != b:
#         print("三角形为等腰三角形")
#     elif b ==c and c != a:
#         print("三角形为等腰三角形")
#     else:
#         print("三角形为普通三角形")
#
# else:
#     print("三边不能构成三角形")

#练习 北京市民采用梯度用电收费，第一档：2880度以下，0.4883元一度；第二档2880-4800，0.5383一度；第三档，4800以上，0.7883一度
#根据输入的用电度数，判断电费
power = input("请输入您本月用电度数:")
dian_fei = 0.4883 or 0.5883 or 0.7883
consumption = int(power) * dian_fei
if int(power) < 2880:
    consumption == int(power) * (dian_fei == 0.4883),  print("你本月消费为:",float(consumption))
elif 2880<=int(power)<=4800:
    consumption == int(power) * (dian_fei == 0.5883), print("您本月消费为:",float(consumption))
elif 4800 < int(power):
    consumption == int(power) * (dian_fei == 0.7883), print("您本月消费为:",float(consumption))


