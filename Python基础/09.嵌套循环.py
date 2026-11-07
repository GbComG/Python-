""""
#循环嵌套，根据输入的长方形长度m，宽度n,打印一个长方形;

#  如下是一个长度为10.宽度为5的长方形
#   * * * * * * * * * * *
    * * * * * * * * * * *
    * * * * * * * * * * *
    * * * * * * * * * * *
    * * * * * * * * * * *
    """
#print("*”)自带换行效果
#print("*",end=""): end表示每一次输出之后以什么结尾，默认 \n 表示换行


#1.接受键盘录入
#长度
# m = int(input("请输入长方形的长度:"))
# #宽度
# n = int(input("请输入长方形的宽度:"))
# for j in range(n):
#     print()
#     for i in range(m):
#         print("*",end = " ")

# #案例，打印出九九乘法表
# i = 0
# for i in range(1,10):
#     print()
#     for j in range(1,i+1):
#         print(f"{i}*{j} = {i*j}",end="\t ") #\t 为制表符

#案例1，根据输入的三角形边长，打印等腰直角三角形
# a = int(input("请输入等腰直角三角形直角边边长:"))

# for i in range(a):
#     # 第i行（从0开始）打印 i+1 个星号，随行数递增
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()  # 每行打印完换行
#案例2，根据输入的数字，打印数字金字塔
# num = int(input("请输入末尾数字:"))
# for i in range(1,num+1):
#     print()
#     for j in range(1,i+1):
#         print(j,end=" ")

#牛逼案例 设计B站用户登陆页面
account = input("请输入用户名:")
password = input("请输入密码:")
while True:
    if account == "admin" and password == "666888":
        print("登陆成功，进入B站首页！")
    elif account == "zhangsan" and password == "123456":
        print("登陆成功，进入B站首页！")
    elif account == "taoge" and password == "888666":
        print("登陆成功，进入B站首页！")



