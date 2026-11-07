# 常量(不会发生变化的数据) ; 常量的名称为全部大写)
PI = 3.1415926
NAME = "黑马★海哥"

# 函数
def log_separator1():  # 2用法
    print("-" * 30) # "-"重复输出30次

def log_separator2():
    print("+" * 30)

def log_separator3():  # 1个用法
    print("#" * 30)

def log_separator4():
    print("*" * 30)

# 测试函数
#__name__,python中的内置函数表示当前模块的名称（直接运行当前模块，它的值为"__main__",将其导入时,__name__的值就是模块名）
print(__name__)
#执行当前文件，则会执行如下代码；如果被当作模块导入，如下代码不执行
if __name__ == "__main__":
    log_separator1()