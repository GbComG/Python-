"""
闭包的背景介绍
    定义一个函数，
"""
#需求:定义函数保存变量10，调用函数返回值并重复累加数值，观察结果
def fun():
    num = 10
    return num

#调用函数，获得返回值
num = fun()
print(num+1)
print(num+2)
print(num+3)
