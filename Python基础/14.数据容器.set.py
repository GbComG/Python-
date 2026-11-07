# #集合 set------->无序  不可重复  可修改
# #定义
# s1 = {5,3,2,0,9,12,43,64,22,5,0}
# print(s1)
# print(type(s1))
# #定义空集合，不能直接用{}会被识别为‘字典’
# s2 = set()
# print(s2)
# print(type(s2))
#操作	含义	样例
# add(..)	添加元素到集合中	s1.add('t')
# remove(..)	移除集合中的指定元素（指定元素不存在将报错）	s1.remove('t')
# pop()	随机删除集合中的元素并返回	e = s1.pop()
# clear()	清空集合	s1.clear()
# difference()	求取两个集合的差集（包含在第一个集合但不包含在第二个集合的元素）	s1.difference(s2)
# union()	求取两个集合的并集	s1.union(s2)
# intersection()	求取两个集合的交集	s1.intersection(s2)
from sklearn.metrics import balanced_accuracy_score

#常见方法
# add(..)	添加元素到集合中
s1 = {100,200,300,400,500,600,700,800}
print(s1)
s1.add(1200)
print(s1)

# remove(..)	移除集合中的指定元素（指定元素不存在将报错）
s1.remove(200)
print(s1)

# pop()	随机删除集合中的元素并返回
e = s1.pop()
print(e)
print(s1)

#clear()	清空集合
s1.clear()
print(s1)

s2 = {"A","B","C","D","E","X","Y"}
s3 = {"C","E","Y","Z"}

# difference()	求取两个集合的差集（包含在第一个集合但不包含在第二个集合的元素）
print(s2.difference(s3))
print(s3.difference(s2))

# union()	求取两个集合的并集
print(s2.union(s3))

# intersection()	求取两个集合的交集
print(s2.intersection(s3))

#案例
# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = {"遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

#1，找出同时选修了法语和艺术的学生
#方式一:
print(f"同时选修了法语和艺术的学生有:{french_set.intersection(art_set)}")
#方式二:
print(f"同时选修了法语和艺术的学生有:{french_set & (art_set)}")

#2,找出同时选修了所有课程的同学
print(f"同时选修了所有课程的同学有:{football_set & art_set & basketball_set & french_set & art_set}")

#3，找出选修了足球，但没有选修了篮球的同学
#方式一
print(f"选修了篮球但没选修足球的同学:{football_set.difference(basketball_set)}")
#方式二  - ----------->求差集
print(f"选修了篮球但没选修足球的同学:{football_set - basketball_set}")
#方式三 集合推导式--->{要添加的数据 for s in set1 if条件}
fab_set3 = { s for s in football_set if s not in basketball_set}
print(fab_set3)
#4,统计每一个学生选修的课程数量
#4.1获取学生名单
all_set = football_set.union(basketball_set).union(french_set).union(art_set)
print(all_set)
#4.2,获取每一个学生选修课的数量
all_list = [*football_set,*basketball_set,*french_set,*art_set]
print(all_list)
for s in all_list:
    print(f"{s}选修了{all_list.count(s)}门课")

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


