#小明买到一个计算器，里面有+ - * / 四种运算模式，根据输入的两个数字和一个运算符号进行运算


# number_1 = float(input("请输入第一个数字："))
# number_2 = float(input("请输入第二个数字："))
# oper = input("请输入运算符(+ - * /)：")
# match  oper:
#     case "+":
#         print(f"{number_1} + {number_2} = {number_1 + number_2}")
#     case "_":
#         print(f"{number_1} - {number_2} = {number_1 - number_2}")
#     case "*":
#         print(f"{number_1} * {number_2} = {number_1 * number_2}")
#     case "/" if number_2 !=0:
#         print(f"{number_1} / {number_2} = {number_1 / number_2}")
#     case _:
#         print("操作不支持！")
#案例，在游戏中根据玩家输入的信息使角色做出对应的操作
an_jian = input("输入操作按键:")
match an_jian:
    case "上"  "W"  "w":
        print("角色向上运动")
    case "下" "S" "s":
        print("角色向下运动")
    case "左" "a" "A":
        print("角色向左运动")
    case "右" "D" "d":
        print("角色向右运动")
    case "跳" " ":
        print("角色跳跃")
    case "攻击" "J" "j":
        print("角色攻击")
    case "推出" "ESC" "esc":
        print("退出游戏")
    case _:
        print("操作不支持！")



