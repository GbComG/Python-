"""
案例：闭包入门

闭包解释：
概述：
内部函数 使用了外部函数的变量，这种写法就称之为闭包。

格式：
def 外部函数(形参列表):
    外部函数底层的局部变量

    def 内部函数(形参列表):
        使用外部函数的变量

    return 内部函数

预习：
1. 函数名 和 函数() 是两个概念，前者表示函数对象，后者表示：调用函数，获取返回值。
"""
#定义一个闭包，外部函数有num1,内部函数有num2,然后调用，并用于求解两数之和，观察效果
def fun_outer(num1):
    def fun_inner(num2):
        #求和
        sum = num1 + num2
        print(f'求和结果:{sum}')
    return fun_inner
fun_inner = fun_outer(5)
fun_inner(20)
