#按要求定义一个可以计算多个数据和字典value值和的函数，并给其友好提示

def friend_tips(fn_name):
    def fn_inner(*args, **kwargs):
        print('正在努力计算中...')
        return fn_name(*args,**kwargs)
    return fn_inner
@friend_tips
def get_sum(*args,**kwargs):
    """
    该函数用于计算 数字列表 和 字典value值之和
    :param args: 数字列表  #*args --> 接受所有的位置参数，封装到元组中
    :param kwargs: 字典，键是字符串，值是数字  **kwargs--> 接受所有的关键字参数，封装到字典中
    :return: 结果之和
    """
    #2.1定义求和变量
    sum = 0
    #2.2遍历元组，获取每一个元素，求和
    for i in args:
        sum += i
    #2.3遍历字典,获得每一个value值
    for j in kwargs.values():
        sum += j
    #2.4返回结果
    return sum

    #上述代码可优化如下
    # return sum(args)+sum(kwargs.values())

print(get_sum(1, 2, 3, a=3,b=4,c=6))