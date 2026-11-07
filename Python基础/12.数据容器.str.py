# # 字符串 基本操作----> 不可变(无法修改)
# s = "Hello-Python"
#
# print(s[4]) #正向索引
# print(s[-8]) #反向索引
#
# # s[4] = "X"
# # print(s[4]) #不可变(无法修改) 会报错!!!
#
# for i in s:
#     print(i)
#
# #--------------------切片--------------------------
# print(s[0:5:1])
# print(s[:5:1])
# print(s[:5:])
# print(s[:5])
#
# print(s[6:12:1])
# print(s[6::1]) #若直接切片到末尾，中间可省略
# #步长------正数为从前往后,负数为从后往前
# print(s[-1:-7:-1])

#“”“ 字符串常用方法
#方法	         作用	                                             样例
# #find()	在字符串中查找子串，返回第一次出现的索引位置，找不到返回 -1	s.find('Python')
# count()	统计子串在字符串中出现的次数	s.count('H')
# upper()	将字符串中的所有字母转换为大写	s.upper()
# lower()	将字符串中的所有字母转换为小写	s.lower()
# split()	将字符串按指定分隔符分割成列表	s.split(' ')
# strip()	去除字符串两端的空白字符或指定字符	s.strip() / s.strip('*')
# replace()	将字符串中的指定子串替换为新的子串	s.replace('H','C')
# startswith()	检查字符串是否以指定子串开头，返回布尔值	s.startswith('P')
# s = "   Hello-Python-Hello-World   "
#
# #1 #find()	在字符串中查找子串，返回第一次出现的索引位置，找不到返回
# index = s.find("-")
# print(index)
# #2 count()	统计子串在字符串中出现的次数
# c = s.count("o")
# print(c)
# #3 upper()	将字符串中的所有字母转换为大写
# su = s.upper()
# print(su)
# #4 lower()	将字符串中的所有字母转换为小写
# sl = s.lower()
# print(sl)
# #5 split()	将字符串按指定分隔符分割成列表
# slist = s.split("-")  #slist =["Hello","Python","Hello","World]
# print(slist)
# #6 strip()	去除字符串两端的空白字符或指定字符
# ss = s.split()
# print(ss)
# #7 replace()	将字符串中的指定子串替换为新的子串
# sr = s.replace("-","~")
# print(sr)
# #8 startswith()	检查字符串是否以指定子串开头，返回布尔值
# print(s.startswith("Hello"))
# print(s.endswith("Python"))
#
# print("-------------------------------------------")
# print(s)  #输出出来不变，字符串不可变

#-------------------------字符串案例---------------------------------
#案例1:邮箱格式验证:用户输入一个邮箱，验证邮箱格式是否正确(包含一个@和至少一个.),如果输入正确，输出邮箱格式正确，否则输出邮箱格式错误

#1.接受用户输入的邮箱
# email = input("请输入您的邮箱:")
# #2.判断邮箱的格式
# if email.count("@") == 1 and email.count(".") >= 1:
#
#     print(f"{email}是合法的邮箱。")
# else:
#     print(f"{email}是不合法的!")
# #方法二-------------  in判断子字符串是否存在字符串中，如果在返回True，不在则返回False
# #1.接受用户输入的邮箱
# email = input("请输入您的邮箱:")
# #2.判断邮箱的格式
# if email.count("@") == 1 and "." in email:
#
#     print(f"{email}是合法的邮箱。")
# else:
#     print(f"{email}是不合法的!")

#案例2 输入一个字符串判断其是不是回文
# 黄山落叶松叶落黄山   上海自来水来自海上
# lan = input("请输入字符串:")
# lan1 = lan[::-1]
# if lan == lan1[::-1]:
#     print("该字符串是回文")
# else:
#     print("该字符串不是回文")
#将用户输入的十个字符串，反转后全部转为大写，并存入列表，再将列表中的遍历出来
new_list = []
for i in range(10):
    s = input(f"请输入第{i+1}个字符串：")
    # 先处理当前字符串：反转文字 + 转大写
    processed_str = s[::-1].upper()
    new_list.append(processed_str)  # 将处理好的字符串存入列表

# 遍历输出
for i in new_list:
    print(i)



