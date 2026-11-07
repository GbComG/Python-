"""
案例:演示多个装饰器装饰一个原函数

记忆：
    多个装饰器装饰一个原函数，是按照由内而外的顺序来装饰的
    但如果你要是用 装饰器的写法来做，看到的效果是：从上往下执行
"""

#发表评论前需要先登录再验证验证码

#1.定义装饰器：验证登录
def check_login(fn_name):
    def login_inner():
        print('校验登录')
        fn_name()
    return login_inner
#2.定义装饰器：验证验证码
def check_code(fn_name):
    def code_inner():
        print('校验验证码')
        fn_name()
    return code_inner

#3.定义原函数:
@check_login
@check_code
def comment():
    print('评论成功')

comment()
