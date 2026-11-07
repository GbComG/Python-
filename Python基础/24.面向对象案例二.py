#练习
# **采用面向对象编程思想完成如下需求**
# - 采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。
# 系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。具体功能如下：
# 1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# 2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
# 3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# 4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
# 5. 退出购物车

#商品类

class Goods:
    def __init__(self,name,price,number):
        self.name = name
        self.price = price
        self.number = number
    def __str__(self):
        return f"商品名称:{self.name},价格:{self.price},购买数量:{self.number}"
    def update_goods(self,name = None,price = None,number = None):
        if name is not None:
            self.name = name
        if price is not None:
            self.price = price
        if number is not None:
            self.number = number

#购物车类
class ShoppingCart:
    shopping_cart_version = 3.0
    def __init__(self):
        self.goods = []
    #1.添加购物车
    def add_goods(self):
        name = input("请输入你要添加的商品:")
        for s in self.goods:
            if s.name == name:
                print("购物车中已存在相同商品，无法重复添加。")
                return
        price = int(input("请输入商品价格:"))
        number = int(input("请输入购买数量:"))
        if price>0 and 1<= number <= 999:
            goods = Goods(name,price,number)
            self.goods.append(goods)
            print("添加成功！")
    #2.修改购物车
    def update_goods(self):
        name = input("请输入要修改的商品信息")
        for s in self.goods:
            if s.name == name:
                print(f"商品信息{s}")
                print("请完成商品信息修改!")
                price = int(input(f"请输入修改后的{name}价格:"))
                number = int(input(f"请输入修改后的购买数量:"))
                if price>0 and 1<= number <= 999:
                    s.update_goods(price=price,number=number)
                    print("修改成功！")
                    print(f"修改后商品信息:{s}")
                    return
                else:
                    print("请确保商品价格大于零且购买数量大于0，小于等于999")
                    return
        print("未查找到对应商品，请重新输入！")
    #3.删除购物车
    def delete_goods(self):
        name = input("请输入你要删除的商品:")
        for s in self.goods:
            if s.name == name:
                self.goods.remove(s)
                print("商品信息删除成功。")
                return
        print("未查找到该商品，删除失败")
    #4.单独查询加入购物车商品
    def show_goods(self):
        name = input("请输入要查询的商品信息:")
        for s in self.goods:
            if s.name == name:
                print(f"查询到商品信息:{s}")
                return
        print("未查找到商品信息")
    #5.查询全部购物车的商品
    def list_goods(self):
            if not self.goods:
                print("购物车空空如也！快去剁手啊喂！")
                return  # ← 记得返回啊バカ！
            for s in self.goods:
                print(s)
    #6.运行
    def run(self):
        print(f"欢迎使用京东购物车,当前版本{ShoppingCart.shopping_cart_version}")


        while True:
            print()
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ")
            print("# 1.添加购物车 2.修改购物车 3.删除购物车 4.查询单个购物车商品 5.查询全部购物车商品 6.退出系统 #")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print()
            print()
            choice = input("请选择您要执行的操作(输入1-6):")
            match choice:
                case "1": #添加
                    self.add_goods()
                case "2": #修改
                    self.update_goods()
                case "3": #删除
                    self.delete_goods()
                case "4": #查询单个
                    self.show_goods()
                case "5": #查询全部
                    self.list_goods()
                case "6": #退出
                    print("Bye")
                    break
                case _:  # 其他情况
                    print("输入错误，请选择1-6进行菜单中的功能")
#测试
if __name__ == '__main__':
    shopping_car = ShoppingCart()
    shopping_car.run()






















