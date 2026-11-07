"""
记忆：
    1.一个装饰器的参数有且只能有一个
    2.如果装饰器有多个参数，可以在该装饰器的外面再包裹一层，把装饰器当作其内部函数返回即可
"""

#定义一个既能装饰减法运算，又能装饰加法运算的装饰器，即带有参数的装饰器

#1.定义装饰器
def logging(flag):
    def my_decorator(fn_name):
        def fn_inner(x,y):
            if flag == '+':
                print('正在努力计算加法中...')
            if flag == '-':
                print('正在努力计算减法中...')
            return fn_name(x,y)
        return fn_inner
    return my_decorator
#2.定义原函数:加
@logging('+')
def add(x,y):
    return x + y
#3.定义原函数:减
@logging('-')
def subtract(x,y):
    return x - y


print(add(10,20))
print(subtract(10,20))