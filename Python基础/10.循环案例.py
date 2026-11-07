#案例1 设计B站用户登陆页面
#关键字 break,只能出现在循环中，表示结束，跳出循环的含义(break跳出循环后,while中的else的代码将不会执行)
#continue,同样只能出现在循环中，表示中断本次循环，直接进入下次循环。
#1，接收输入的用户名
# while True:
#     account = input("请输入用户名:")
#     password = input("请输入密码:")
# #2，用户名和密码不能为空！
#     if account == " " or password == " ":
#         print("输入的用户名和密码不能为空！")
#         continue #结束循环，进入下一轮循环
# #3，判断用户名和密码是否正确,执行登陆操作
#     if account == "admin" and password == "666888":
#         print("登陆成功，进入B站首页！")
#         break #跳出循环
#     elif account == "zhangsan" and password == "123456":
#         print("登陆成功，进入B站首页！")
#         break #跳出循环
#     elif account == "taoge" and password == "888666":
#         print("登陆成功，进入B站首页！")
#         break #跳出循环
#     else:
#         print("用户名或密码不正确，请重新输入")

#案例2
#猜数字游戏
#系统随机生成一个数字，用户根据系统提示猜数字,并将数字输入系统,如果猜错,系统根据大小进行提示,如果猜对,退出系统,游戏结束
# 导入放最开头
import random

print("欢迎来到猜数游戏,系统随机生成一个数字，用户根据系统提示猜数字,并将数字输入系统,如果猜错,系统根据大小进行提示,如果猜对,退出系统,游戏结束")
while True:
    zhi_ling = input("请确认是否进入游戏（是/否）：")
    if zhi_ling == "否":
        exit()
    elif zhi_ling == "是":
        random_number = random.randint(1,100)
        # 【关键缩进】猜数字循环必须缩在是分支内部
        while True:
            num = int(input("请输入一个数字:"))
            if num > random_number:
                print("你所猜数字要大于答案！")
            elif num < random_number:
                print("你所猜数字要小于答案！")
            elif num == random_number:
                print("恭喜您完成游戏！")
                ming_ling=input("是否要再次游戏?(是或否):")
                if ming_ling == "是":
                    print("数字已重新生成，请开始新一轮游戏！")
                    break
                elif ming_ling == "否":
                    print("游戏结束，再见！")
                    exit()
    else:
        print("请再次确认")
