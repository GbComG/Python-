"""
案例：演示封装之私有属性

封装简介：
    概述：
        属于面向对象的三大特征之一
    怎么封装？
        我们学的函数，类都是封装的体现.
    好处:
        1.提高代码的安全性。 由私有化来保证
        2.提高代码的复用性。 由函数来决定
    弊端：
        代码量增加了，因为私有内容外界想访问，必须提供公共的访问方式，代码量就增加了。
"""
# 小明把技术给徒孙的时候，不想把私房钱给徒孙，代码模拟

#1.定义徒弟类
class prentice:
    #1.属性
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'
        self.__money = 500000
    #2.方法
    def make_cake(self):
        print(f"用{self.kongfu}摊煎饼")
    #3.3 针对私有的属性，提供公共的访问方式
    def getmoney(self):
        return self.__money
#2.定义徒孙类
class Tusun(prentice):
    pass
#测试
if __name__ == '__main__':
    tsun = Tusun()
    print(tsun.kongfu)
    tsun.__money = -100
    print(tsun.getmoney())