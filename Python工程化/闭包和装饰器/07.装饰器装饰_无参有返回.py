#需求：定义无参有返回的的get_sum求和函数,在不改变其代码的基础上，添加友好提示：正在努力计算中...

def friend_tips(fn_name):
    def fn_inner():
        print('正在努力计算中...')
        return fn_name()
    return fn_inner

@friend_tips
def get_sum():
    a= 10
    b= 20
    return a + b

sum = get_sum()
print(sum)


