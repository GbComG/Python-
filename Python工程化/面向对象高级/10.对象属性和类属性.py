"""
案例：演示对象属性和类属性

属性介绍：
    概述：
        它是一个名词，用来描述事物的外在特特征的
    分类：
        对象属性：属于每个独对象的，即：每个对象的属性值可能不同，修改A不影响B。
        类属性： 属于类的，即：能被该类下所有的对象共享，A对象修改类属性，B对象访问的是修改后的

对象属性：
    定义到init魔法方法中的属性，每个对象都有自己的内容

类属性：
    定义到类中函数外的属性（变量），能被该类下所有的对象所共享。
    既能通过类名，还能通过对象名的方式来调用，推荐使用类名.的格式
"""
#1.定义一个Student类
class Student(object):
    #1.1定义类属性
    teacher_name = '水镜先生'

    #1.2定义对象属性
    def __init__(self,name,age):
        self.name=name
        self.age=age
    #1.3定义str魔法方法，输出对象的信息
    def __str__(self):
        return f'姓名:{self.name},年龄: {self.age}'
#2.测试
if __name__=='__main__':
    #场景一：对象属性

    # s1 = Student('曹操',38)
    # s2 = Student('曹操',38)
    # print(s1)
    # print(s2)
    # #输出结果一致

    #修改后

    s1 = Student('许褚',48)
    s2 = Student('曹操',38)
    print(s1)
    print(s2)
    #s1修改后不影响s2

    #场景二：类属性
    print(s1.teacher_name)
    print(s2.teacher_name)

    print('-'*23)

    s1.teacher_name = '老王子'
    print(s1.teacher_name) #老王子
    print(s2.teacher_name) #水镜先生

    Student.teacher_name = '老王子'
    print(s1.teacher_name)
    print(s2.teacher_name) 
