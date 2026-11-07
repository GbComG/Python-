def my_decorator(fn_name):
    def fn_inner(x,y):
        if fn_name.__name__ == 'add':
                print('正在努力计算加法中...')
        if fn_name.__name__ == 'subtract':
            print('正在努力计算减法中...')
        return fn_name(x,y)
    return fn_inner
#2.定义原函数:加
@my_decorator
def add(x,y):
    return x + y
#3.定义原函数:减
@my_decorator
def subtract(x,y):
    return x - y


print(add(10,20))
print(subtract(10,20))