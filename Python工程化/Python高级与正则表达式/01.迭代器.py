"""
案例：演示自定义迭代器

迭代器介绍:
    概述:
        自定义的类，只要写了__iter__()和__next__()方法，就可以成为迭代器
    目的:
        隐藏底层的逻辑，让用户使用更方便,
        惰性加载，用的时候才会获取
"""
from turtledemo.round_dance import stop

#需求:模拟range(1,6) 自定义迭代器实现同等逻辑
#场景1：回忆range写法
for i in range(1,6):
    print(i)
print("-"*30)

#场景2:自定义迭代器
#1.自定义迭代器类
class MyIterator:
    #2.通过init方法，初始化属性，指定:范围
    def __init__(self, start,end):
        self.current_value = start  #当前值默认为开始值
        self.end_value = end    #结束值
    #3.通过重写iterator魔法方法，返回当前对象(即:迭代器对象)
    def __iter__(self):
        return self
    #4.重写next魔法方法，返回当前值，并更新当前值
    def __next__(self):
        #4.1判断当前值是否合法
        if self.current_value >= self.end_value:
            raise StopIteration #抛出异常，迭代结束
        #4.2走这里，说明当前值合法，返回当前值，并更新当前值
        value = self.current_value
        self.current_value+=1
        return value

#5.创建迭代器对象并遍历
#5.1
for i in MyIterator(1,6):
    print(i)
print('-'*30)

#5.2 next()函数
my_itr = MyIterator(1,6)
print(next(my_itr))
print(next(my_itr))
print(next(my_itr))
print(next(my_itr))
print(next(my_itr))