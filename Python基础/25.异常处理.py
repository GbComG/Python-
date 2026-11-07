try:
    print("----------------------")
    print(my_name)
    print("----------------------")
except NameError as e: #捕获的是 NameError 类型的错误
    print("程序运行出错，请联系管理员:异常信息:",e)


try:
    (print("----------------------"))
    #print(my_name)
    # print(1/0)
    # print("ABC"[10])
    print("ABC".hello)
    print("----------------------")
except NameError as e:
    print("名字不存在，请检查变量或函数的名字，异常信息:",e)
except ZeroDivisionError as e: #捕获的是 ZeroDivisionError 类型的错误
    print("0不能做被除数:异常信息:",e)
except IndexError as e:
    print("索引错误，异常信息:",e)
except Exception as e:
    print("程序出错了，请联系管理员，错误信息:",e)
finally: #无论程序是否正常运行，finally代码块中的代码都会正常循行
    print("资源释放")

#异常的传递
# 异常的传递
def fun1():
    print("fun1 ... running ...")
    fun2()

def fun2():
    print("fun2 ... running ...")
    fun3()

def fun3():
    print("fun3 ... running ...")
    print(my_color)


if __name__ == '__main__':
    try:
        fun1()
    except Exception as e:
        print("程序运行出错了，请联系管理员，错误信息：", e)
