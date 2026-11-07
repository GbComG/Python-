#for循环--遍历输入的字符串

# msg = input("请输入需要遍历的字符串:")
# for i in msg: #i表示遍历出来的元素，msg是被遍历的数据
#     print(f"元素{i}")
# else:
#     print("输出完成")

#计算1——100之间所有奇数之和

#原始
# total = 0
# range(1,101)
# i=1
# for i in range(1,101):
#     if i % 2 == 1: #奇数
#         total += i
#     print(total)
# else:
#     print("end")
#
# #简化
# total = 0
# range(1,101,2)
# for i in range(1,101,2):
#     total += i
#     print(total)

#案例2 计算100-500之间所有3的倍数的累加之和
total = 0
range(100,501)
for i in range(100,501):
    if i % 3 == 0:
        total += i
    print(total)