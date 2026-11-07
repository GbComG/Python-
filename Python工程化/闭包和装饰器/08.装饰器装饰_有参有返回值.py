#需求：定义有参有返回的的get_sum求和函数,在不改变其代码的基础上，添加友好提示：正在努力计算中...
def friend_tips(fn_name):
    def fn_inner(x,y):
        print('正在努力计算中...')
        return fn_name(x,y)
    return fn_inner
@friend_tips
def get_sum(x,y):
    return x + y
"""
#传统写法
get_sum = friend_tips(get_sum)
print(get_sum(10,20))
"""
#语法糖写法
print(get_sum(10,20))