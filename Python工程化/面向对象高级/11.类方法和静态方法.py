"""
## 1. 类方法

属于类的方法，可以通过 类名 调用，也可以通过 对象名 调用。
定义类方法时，必须加装饰器：`@classmethod`，且第一个参数代表类对象（约定写 cls）**。

## 2. 静态方法

属于类下所有对象共享的方法，可以通过 类名 调用，也可以通过 对象名 调用。
定义静态方法时，必须加装饰器：`@staticmethod`，**没有强制要求的固定首参数**，参数可空、自定义。

## 3. 两者区别

1. 类方法第一个参数必须是类对象；静态方法没有参数强制要求。
2. 使用判断思路：如果函数内部需要使用**类属性**，就定义成类方法；否则定义成静态方法，除此之外调用方式基本无差别。
"""
class Student(object):
    school = '黑马程序员'
    #定义类方法
    @classmethod
    def show1(cls):
        print(f'cls:{cls}')
        print('我是类方法')
    #定义静态方法
    @staticmethod
    def show2():
        print('我是静态方法')
#测试
if __name__ == '__main__':
    s1=Student()
    print(s1.school)
    s1.show1()
    print('-'*25)
    s1.show2()