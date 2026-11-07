"""
案例：演示单继承，即一个子类继承有一个父亲

故事一：一个摊煎饼的老师傅，在煎饼果子界摸爬滚打多年了，研发了一套精湛的摊煎饼技术，师傅要把这个技术传授给他唯一的最得意的徒弟

"""

#定义师傅类
class Teacher(object):
    def __init__(self):
        self.kongfu = '[古法配方]'
    def make_cake(self):
        print(f"采用{self.kongfu}摊煎饼果子")

#定义徒弟类继承自师傅类
class Prentice(Teacher):
    pass

#3.测试
p = Prentice()
p.make_cake()