#--------------------------------------函数  变量的作用域---------------------------------------
#全局变量
# num = 100
#
#
# #定义函数
# def circle_area(r):
#     #局部变量
#     pi = 3.14
#     area = pi * r * r
#     #局部变量
#     global num #global 声明全局变量，先声明后使用
#     num = 10000
#     print("num=", num)
#     return area
#
# #调用函数
# print("num=",num) #num == 10000
# c_area = circle_area(10)
# print(c_area)

#----------------------------函数  传参---------------------------------
#定义函数
# def reg_stu(name,age,gender,city):
#     print(f"注册成功，姓名{name},年龄{age},性别{gender},城市{city}")
#     return{"name":name,"age":age,"gender":gender,"city":city}
#
# #传参方式一:位置参数
# stu = reg_stu("张三",18,"男","北京")
# print(stu)
#
# #传参方式二:关键字传参
# stu =reg_stu(name="王林",age=28,gender="男",city="北京")
# print(stu)
#
# #传参方式三:位置参数+关键字参数------->使用时位置参数在前，关键字参数在后
# stu =reg_stu("李慕婉",19,gender="女",city="北京")
# print(stu)
#
# #-------------------函数不定长参数(*args)----------------------------
# #根据输入的这批数据，计算最小值，最大值，平均值
# def calc_data(*args):
#     min_data = min(args)
#     max_data = max(args)
#     avg_data = sum(args)/len(args)
#     return min_data,max_data,avg_data
#
# #调用函数
# calc_data(2,7,9.10,75)
# print(calc_data(2,7,9.10,75))
# calc_data(2,7,9.10,75,73,37,93,92,111,222)
# print(calc_data(2,7,9.10,75,73,37,93,92,111,222))

#----------------------函数 不定长参数(关键字参数 **kwargs---->封装到字典中)
def calc_data(*args,**kwargs):
    """
    :param args:不定长位置参数，需要计算的这批数据
    :param kwargs:不定长关键字参数
        round:保留的小数位个数
        print:是否打印输出
    :return:最小值，最大值，平均值
    """
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args)/len(args)
    if kwargs.get("round") is not None:
        avg_data = round(avg_data,kwargs.get("round"))
    if kwargs.get("print"):
        print(f"最大值:{min_data},最小值:{max_data},平均值:{avg_data}")
    return min_data,max_data,round(avg_data,1)

#调用函数

print(calc_data(2,7,9.10,75,round=3,print=True))

# print(calc_data(2,7,9.10,75,73,37,93,92,111,222))




