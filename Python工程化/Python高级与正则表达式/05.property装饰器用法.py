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
"""
#需求：定义学生类,私有属性age,通过property实现简化调用
#1.定义学生类
class Student():
    #1.1私有属性
    def __init__(self):
        self.__age = 18
    #1.2提供公共的访问方式
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        #可以在这里对传入的age值做判断,但是一般不做，重要学段才会做判断
        #因为实际开发中数据是从前端传过来的，已经做过判断了，这里属于二次校验.
        self.__age = age

#2.测试
if __name__ == '__main__':
    #2.1创建学生对象
    stu = Student()
    #2.2设置值
    stu.age = 20
    #2.3获取值
    print(stu.age)
