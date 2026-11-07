#函数的参数类型
# 加
# def add(x, y):
#     return x + y
#
# # 减
# def subtract(x, y):
#     return x - y
#
# # 乘
# def multiply(x, y):
#     return x * y
#
# # 除
# def divide(x, y):
#     return x / y
#
# # 计算
# def calc(x, y, oper):
#     return oper(x, y)
#
# calc(10, 20, add)
# print(calc(10,20,add))

#---------------匿名函数---------------
#将一个列表中的元素按从小到大开始排列
# data_list = ["c++","c","python","php","jack","go","javascript","java","rust"]
# data_list.sort()
# print(data_list)
# data_list.sort(key = lambda item: len(item))
# print(data_list)

#-------------------------------递归------------------------------------
#案例1:计算n的阶乘
#递归调用.指的是在函数中自己调用自己的情况---->一定得有终结点
# def jc(n):
#     return jc(n) * jc(n-1)

#案例 定义一个函数，用于根据传入的一批商品信息（商品名.价格.数量）,优惠（优惠券，积分抵扣），运费信息计算订单的总金额
#具体规则如下：
#1.优惠券需要商品额满5000才可以使用，且优惠金额不能超过商品总价。
#2.积分折扣需要商品总金额满5000才可以使用，100积分抵扣1元（且折扣金额不能超过商品总价，积分只能整百抵扣）

def shoping_list(name,price,members,yun_fei):
    ji_fen = int(input("积分为:"))
    if  price >= 5000:
        you_hui = ji_fen // 100
        zong_jia = price * members + yun_fei - you_hui
        return zong_jia
    else:
        zong_jia = price * members + yun_fei
        return zong_jia
result = shoping_list(name = input("请输入商品名称:"),price = int(input("商品金额为：")),members = int(input("购买数量:")),yun_fei = int(input("运费金额:")))
print("商品金额为",result)
