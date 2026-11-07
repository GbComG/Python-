#函数定义，函数定义的时候不会执行，只有在调用函数的时候，函数体的逻辑才会执行；函数必须先定义，后调用；
#
# def out_line():
#     print("--------------------------------------")
#     print("--------------------------------------")
#
# #函数调用
#
# out_line()
from scipy.cluster.hierarchy import average


#函数的参数与返回值
#函数一：计算圆的面积--半径
def circle_area(r):
    area = 3.14 * r**2
    return area
circle_area(10)
print(circle_area(10))

#函数二：计算长方形的面积--长，宽
def rectangle_area(l,w):
    area = l * w
    return area
area = rectangle_area(10,10)
print(area)

#函数三：计算圆的面积，周长--半径---->如果返回值有多个，多个返回值之间逗号分离----多个返回值会封装到元组之中
def circle_area(r):
    return 3.14 * r**2 , round(2 * 3.14 * r,1)
al = circle_area(10)
print(al)
print(type(al))

area,len = circle_area(10)
print(area)
print(len)

#函数的嵌套调用
def function_a():
    print("a......before")
    function_b()
    print("a......after")
def function_b():
    print("b......before")
    function_c()
    print("b......after")
def function_c():
    print("c......before")

function_a()

print("函数调用完毕")




