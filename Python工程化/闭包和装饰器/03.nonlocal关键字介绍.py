"""
nonlocal 关键字介绍:
    他是Python内置的关键字，可以实现在内部函数修改外部函数的变量
"""
#编写一个闭包，让内部函数访问外部函数的参数，a=100，并观察结果

def fun_outer():
    a=100
    def fun_inner():
        nonlocal a
        print(f'外部函数变量{a}')
        a+=1
        print(f'修改后外函数变量{a}')

    return fun_inner

fun_inner = fun_outer()
fun_inner() #101
fun_inner() #102
