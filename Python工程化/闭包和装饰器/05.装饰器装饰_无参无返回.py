"""
案例:装饰器装饰_无参无返回的原函数

细节:
    装饰器的内部函数格式 要和 被装饰的函数的格式一致
"""
#需求：定义无参无返回的的get_sum求和函数,在不改变其代码的基础上，添加友好提示：正在努力计算中...

#1. 定义装饰器
def friend_tip(fn_name):
    def fn_inner():
        print('正在努力计算中...')
        fn_name()
    return fn_inner
#2. 定义原函数
@friend_tip
def get_sum():
    a = 10
    b = 20
    sum = a + b
    print(f'结果:{sum}')

get_sum()
