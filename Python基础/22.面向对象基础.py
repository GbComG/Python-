#定义类----->不推荐 动态的为对象添加属性
# class Car:
#     pass
#
# #创建对象
# c1 = Car()\
# #动态的为对象添加属性
# c1.color = "red"
# c1.brand = "BMW"
# c1.name = "x5"
# c1.price = 500000
# print(c1)
# print(c1.brand)
# print(c1.__dict__)#会将对象中的所有属性以字典的形式输出出来
#
# #定义类
# class Car:
#     #__init__方法是初始化方法,会在对象生成时自动调用，可以在该方法中为对象设置对性的属性;
#     #self是第一个参数，表示当下创建出来的实例对象
#     def __init__(self,color,brand,name,price):
#         self.color = color
#         self.brand = brand
#         self.name = name
#         self.price = price
#         print("Car类型的对象初始化完成，对象属性已添加完毕")
# #创建对象
# c1 = Car("red","BMW","x7",800000)
# print(c1.__dict__)

#-----------------------------------定义类 实例方法-----------------------------------\
class Car:
    def __init__(self,c_color,c_brand,c_name,c_price):
        self.c_color = c_color
        self.c_brand = c_brand
        self.c_name = c_name
        self.c_price = c_price
        print("Car类型的对象初始化完毕，对象属性已添加完毕")
    #定义实例方法
    def running(self):
        print(f"{self.c_brand}{self.c_name}正在高速行驶中")