"""
子类重写功能后，继续访问父类功能

思路:
    1.父类名.父类函数名(self) 精准访问，想找哪个父类就调用
    2.super().父类函数名()   只能访问最近的父类
"""

class Master(object):
    def __init__(self):
        self.kongfu = "[古法配方]"
    def make_cake(self):
        print(f"采用:{self.kongfu}摊煎饼果子")
#2.定义黑马学校类
class School(object):
    def __init__(self):
        self.kongfu=("[黑马AI煎饼果子配方]")
    def make_cake(self):
        print(f"采用:{self.kongfu}摊煎饼果子")

#3.定义徒弟类，有个对象叫小明
class Student(Master, School):
    def __init__(self):
        self.kongfu="[自制配方]"
    def make_cake(self):
        print(f"食用:{self.kongfu}摊煎饼果子")
    def make_master_cake(self):
        Master.__init__(self)  #有__init__被调用时就覆盖，没有就不变
        Master.make_cake(self)
    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

class Tusun(Student):
    pass
#4.测试
if __name__ == '__main__':
    XM=Student()
    print(XM.kongfu)  #独创
    XM.make_cake() #独创
    XM.make_master_cake() #古法
    XM.make_school_cake() #AI
    print("-"*34)
    XM.make_cake() #AI  被覆盖了