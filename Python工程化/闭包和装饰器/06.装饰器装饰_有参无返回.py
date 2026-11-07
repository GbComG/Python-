#需求：定义无参无返回的的get_sum求和函数,在不改变其代码的基础上，添加友好提示：正在努力计算中...

#定义装饰器
def friend_tips(fn_name):
    def fn_inner(x,y):
        print('正在玩命计算中...')
        fn_name(x,y)
    return fn_inner

#定义元原函数（有参无返回值）
@friend_tips
def get_sum(a,b):
    sum = a+b
    print(f'{a} + {b} = {sum}')

get_sum(1,2)
