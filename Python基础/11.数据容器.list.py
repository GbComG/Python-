# #列表操作
# #定义列表--list
# from sklearn.decomposition import dict_learning
#
# s = [67 , 56 , True , "hello"]
# print(type(s))
# #获取
# print(s[1]) #正向索引，第二个元素
# print(s[2]) #正向索引，第三个元素
# print(s[-1])#反向索引，第四个元素
# #若使用的索引超出范围，系统报错
# #print(s[10])
#
# #修改
# s[3] = "world"
# print(s[3])
#
# #删除
# del s[2]
# print(s)
#
# #遍历
# # for i in s:
# #     print(i)
#
# #----------------list切片-------------------
# #定义列表
# s = ["A","C","H","K","L","B","D","X","C","U"]
# #切片操作 s[开始索引:结束索引:步长] 左闭右开
# print(s[0:5:1])
# print(type(s[0:5:1]))
# print(s[:5:1])
# print(s[:5:])
# print(s[:5])
# print(s[5])  #切片时，最前方的:不能省略，否则含义发生变化，变为获取列表中的第六个元素
#
# print(s[0:5:2])
# print(s[0:-2:]) #利用反向索引进行切片
#
# #-----------------------------列表list常用方法------------------------------------
#
# # 方法	作用	样例
# # append()	在列表的尾部追加元素	s.append(10086)
# # insert()	在指定索引之前，插入该元素	s.insert(0, 92)
# # remove()	移除列表中第一个匹配到的值	s.remove(75)
# # pop()	删除列表中指定索引位置的元素（如果未指定索引，默认删最后一个）	s.pop(2) / s.pop()
# # sort()	对列表进行排序（列表元素的数据类型一致，才可以进行排序）	s.sort()
# # reverse()	反转列表元素	s.reverse()
#
# s = [56,90,88,65,90,100,209,72,145]
# print(s)
#
# #append() 在列表的尾部追加元素
# s.append(188)
# print(s)
#
# #insert() 在指定的索引之前插入该元素
# s.insert(1,72)
# print(s)
#
# #remove() 移除列表中第一个匹配到的值
# s.remove(90)
# print(s)
#
# #pop() 删除列表中指定索引位置的元素（如果未指定索引，默认删最后一个）
# e = s.pop(1)
# print(e)
# e = s.pop(3)
# print(e)
# print(s)
#
# #sort() 对列表进行排序(列表元素的数据类型一致，才可以进行排序)
# s.sort()
# print(s)
#
# #reverse()	反转列表元素
# s.reverse()
# print(s)
# from numpy.ma.extras import average
#
# #案例 用户输入十个数字，存储到一个列表中，并将列表中的数字进行排列，输出其中的最大值和最小值
# #1 定义列表
# num_list = []
# #2 用户输入的十个数字存入列表
# for i in range(10):
#     num = int(input(f"请输入第{i+1}个有效数字:"))
#     num_list.append(num)
#     print(num_list)
# #3 排序
# num_list.sort()
# print(num_list,"已将数据进行排列")
# #输出最大值最小值和平均值  sum()--->求和，len--->获取元素的个数（列表的长度）--length
# min = num_list.pop(0)
# max = num_list.pop()
# print("最小值为",min), print("最大值为",max)
# ave = average(num_list)
# print("列表内数据平均值为",ave)
# print("列表内数据平均值为",sum(num_list)/len(num_list)) #求平均值！

#案例2 合并两个列表里的元素，并对列表中的元素进行去重处理
# num_list1 = [19,23,54,64,875,20,109,232,123,54]
# num_list2 = [55,80,72,35,60,123,54,29,91]
# #1 合并列表
# for num in num_list2:
#     num_list1.append(num)
# print("整合后的原始列表:",num_list1)
#
# #2去重
# new_list = [] #去重复记录后的列表
# for num in num_list1:
# #判断数字是否在新的列表,如果存在，则返回TRUE,如果不存在，返回FALSE
#     if num not in new_list:
#         new_list.append(num)
# print("去重复记录后的列表",new_list)


# #案例2（简化版） 合并两个列表里的元素，并对列表中的元素进行去重处理
# num_list1 = [19,23,54,64,875,20,109,232,123,54]
# num_list2 = [55,80,72,35,60,123,54,29,91]
# #1 合并列表
# #解包，将列表这一类容器拆解为一个一个独立元素
# #组包，将多个值合并到一个容器里
# num_list = [*num_list1,*num_list2]
# print("整合后的原始列表:",num_list)
#
# #2去重
# new_list = [] #去重复记录后的列表
# for num in num_list1:
# #判断数字是否在新的列表,如果存在，则返回TRUE,如果不存在，返回FALSE
# #     if num not in new_list:
# #         new_list.append(num)
# # print("去重复记录后的列表",new_list)
#
# ##案例2 合并两个列表里的元素，并对列表中的元素进行去重处理
# num_list1 = [19,23,54,64,875,20,109,232,123,54]
# num_list2 = [55,80,72,35,60,123,54,29,91]
# #1 合并列表
# num_list = num_list1 + num_list2
# print("整合后的原始列表:",num_list)
#
# #2去重
# new_list = [] #去重复记录后的列表
# for num in num_list1:
# #判断数字是否在新的列表,如果存在，则返回TRUE,如果不存在，返回FALSE
#     if num not in new_list:
#         new_list.append(num)
# print("去重复记录后的列表",new_list)

#案例3  生成1-20的平方列表
#方式1
list1 = []
for i in range(21):
    list1.append(i ** 2)
    print(list1)
#方式2  列表推导式------>就是按照一定的规则快速生成一个列表的方法-->语法格式: [要插入的值 for i in 序列/列表]
num_list = [i**2 for i in range(21)]
print(num_list)
#案例4 从一个数字列表中提取所有偶数，并计算出平方，组成一个新的列表
num_list2 = [12,32,45,77,80,92,33,57,97,98]
new_list = []
for i in num_list2:
    if i%2 == 0:
        new_list.append(i)
        print("提取后的列表",new_list)
new_list2 = [i**2 for i in new_list]
print("计算平方后的列表",new_list2)
#案例4（简写）列表推导式------>就是按照一定的规则快速生成一个列表的方法-->语法格式: [要插入的值 for i in 序列/列表 if.....]
num_list2 = [12,32,45,77,80,92,33,57,97,98]
new_list = [i**2 for i in num_list2 if i%2 == 0]
print(new_list)


