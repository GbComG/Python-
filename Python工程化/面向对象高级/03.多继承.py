"""
小明是个爱好学习的好孩子，想学习更很多的摊煎饼果子技术，于是，在百度搜索到黑马程序员学校，报班来学习摊煎饼果子技术
"""

#1.定义师傅类
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
    pass

#4.测试
XM = Student()
print(XM.kongfu)
XM.make_cake()