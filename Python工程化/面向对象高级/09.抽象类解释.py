"""
案例：演示抽象类 / 接口

概念:
在 Python 中，抽象类 = 接口；抽象类里面的方法是抽象方法，也叫接口。
抽象方法：没有方法体的方法，用 `pass` 占位。
作用:
抽象类一般作为父类，用于约定业务规范，具体的实现交给子类来完成。

例子（空调）**
父类（抽象类 / 接口）定标准：

- 可以制冷
- 可以制热
- 左右摆风
- ……

简单说：父类定好**必须有哪些方法**，子类必须实现这些方法。
"""
#1.定义父类空调
class AC:
    #1.1制冷
    def coll_wind(self):
        pass
    #1.2制热
    def hot_wind(self):
        pass
    #1.3左右摆风
    def swing_wind(self):
        pass

#2.定义小米空调子类
class Xiaomi(AC):
    def coll_wind(self):
        print('小米 核心 制冷技术')
    def hot_wind(self):
        print('小米 核心 制热技术')
    def swing_wind(self):
        print('小米空调 静音左右摆风 技术')

#3.定义格力空调子类：
class Gree(AC):
    def coll_wind(self):
        print('格力 核心 制冷技术')
    def hot_wind(self):
        print('格力 核心 制热技术')
    def swing_wind(self):
        print('格力空调 低频左右摆风 技术')
#4.测试
if __name__ == '__main__':
    #4.1 小米空调
    xiaomi = Xiaomi()
    xiaomi.coll_wind()
    xiaomi.hot_wind()
    xiaomi.swing_wind()
    print('-'*40)
    #4.2 格力空调
    gree = Gree()
    gree.coll_wind()
    gree.hot_wind()
    gree.swing_wind()
