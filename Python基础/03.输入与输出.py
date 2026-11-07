#获取键盘上输出的数据---input(....)

# name = input("请输入您的姓名:")
# age = input("请输入您的年龄:")
# print(f"您的姓名是:{name}")
# print(f"您的年龄是:{age}")

#案例

#总余额
total = 10000
#输入密码
password = input("请输入您的密码:")
print(f"密码正确:{password}")
#输入取款金额
num = input("请输入取款金额:")
#计算余额 需将num变量str格式转为int---- int(...)
print(f"取款成功，您的余额为：",total - int(num))
