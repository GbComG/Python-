"""
学生管理系统：
        用于记录学生类，学生的属性为：姓名，性别，年龄，手机号，描述信息
"""
from jedi.inference import names


#1.定义学生类
class Student(object):
    #2.定义魔法方法，初始化属性信息
    def __init__(self,name,age,sex,phone,desc):
        self.name=name
        self.age=age
        self.sex=sex
        self.phone=phone
        self.desc=desc
    #3.定义魔法方法，用于打印学生信息
    def __str__(self):
        return f"学生姓名:{self.name},性别:{self.sex},年龄:{self.age},手机号:{self.phone},描述信息:{self.desc}"


#4.测试
if __name__=='__main__':
    s = Student('小王',18,'男',15532291853,'大迫杰')
    print(s)
