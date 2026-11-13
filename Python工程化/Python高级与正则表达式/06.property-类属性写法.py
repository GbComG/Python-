"""
案例:演示property属性的装饰器写法

property属性介绍:
    概述/目的/作用:
        把函数当做变量来使用。
    实现方式:
        方式1：装饰器.
        方式2:类属性.

property的装饰器用法:
    @property    修饰 获取值的函数
    @获取值的函数名.setter    修饰 设置值的函数

    之后就可以直接用上述的函数名来当作变量使用.

property类属性的用法:
    类属性名 = property(获取值的函数名,设置值的函数名)

    之后，就可以直接 上述的函数名 来当作变量直接使用
"""

#需求，定义学生类，私有age属性,通过property充当类属性使用
#1.定义学生类
class Student():
    def __init__(self):
        self.__age=18
    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age=age
    #封装上述的公共方式为类属性:
    #参1：获取值的函数名，参2：设置值的函数名
    hg = property(get_age,set_age)
#测试
if __name__=="__main__":
    stu=Student()
    stu.age = 90
    print(stu.age)