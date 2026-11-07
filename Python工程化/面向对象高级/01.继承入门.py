"""
Father类有一个默认性别为男，且爱好散步行走，那么，son类也想拥有这样的性别和行为

当子类继承父类时，子类Son拥有和父类Father完全一样的功能，但是却不用再写大量重复代码
继承的作用：
好处：提高代码的复用率，减少重复代码的书写。
坏处：耦合性增强了，父类不好的内容，子类同样具备

扩展：开发原则
高内聚，低耦合
    内聚：指的是自己独立处理问题的能力
    耦合：指的是类与类之间的关系
    自己能够搞定的就不要麻烦别人
"""
#定义父类
class Father(object):
    def __init__(self):
        self.gender = "男"
    def walk(self):
        print("饭后走一走，活到九十九")
    def smoking(self):
        print("抽烟有害健康")

#定义子类
class Son(Father):
    pass

s = Son()
print(f"性别:{s.gender}")
s.walk()
s.smoking()

