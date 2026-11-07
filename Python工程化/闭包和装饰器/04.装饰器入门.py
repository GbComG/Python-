"""
装饰器入门：
装饰器介绍：
    概述：
        本质闭包，目的是不改变原有函数功能的基础上增添新的功能
    前提条件：
        1.有嵌套
        2.有引用
        3.有返回
        4.有额外功能
    装饰器用法：
        格式1（传统写法）：
            装饰后的函数名=装饰器名（被装饰函数名）
            装饰后的函数名（）

        格式2（语法糖）：
            在要被装饰的原函数上，直接写@装饰器名，之后直接调用原函数即可
"""
#需求 发表评论前，先要登录

#1.定义外部函数，形参列表接受要被装饰的函数名
def check_login(fn_name): #fn_name 表示要被装饰的函数名(对象) payment comment
    #1.1定义内部函数
    def fn_inner():
        #1.2 额外功能
        print('校验登录...登陆成功')
        #1.3 返回原函数，即：外部函数的引用
        fn_name()
    #1.4返回内部函数对象
    return fn_inner
#2.
@check_login
def payment():
    print('支付成功.')
def comment():
    print('发表评论.')

#3.1 传统写法
comment = check_login(comment)
comment()
#3.2 语法糖写法
print('-'*30)
payment()