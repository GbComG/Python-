"""
案例:演示子类重写父类的功能
    子类有就用子类，没有就调用就近的继承自父类的功能,依次查找，有就用，没有就报错
"""

#小明掌握了老师傅和黑马程序员的配方后，自己又钻研了一套全新的配方

class Master(object):
    def __init__(self):
        self.kongfu = "[古法配方]"
    def make_cake(self):
        print(f"采用:{self.kongfu}摊煎饼果子")
#2.定义黑马学校类
class School():
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

XM = Student()
print(XM.kongfu)
XM.make_cake()