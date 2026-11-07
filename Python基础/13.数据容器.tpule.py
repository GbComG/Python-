#元组基本操作---tpule  元素可以重复，有序，不可修改
#定义  元组不支持修改
import math

t1 = (80,95,78,50,76,80,85,20)
print(t1)
print(type(t1))

# t1[0] = 100
# print(t1)  会报错，元组不支持修改
#
# #切片
# print(t1[0:5:1])
# #count--------统计元素所占个数
# print(t1.count(80))
# #index--------查找指定元素的索引(第一次出现)
# print(t1.index(80))
#
# #注意 如果定义单元素的元组，单个元素之后需要加上,例如 t4 = (100,)
# t3 = ()
# print(t3)
# print(type(t3))
#
# t4 = (100)
# print(type(t4))
# t4 = (100,)
# print(type(t4))

# #定义元组，组包
t1 = (5,7,9,1)
# #定义元组，组包
t2 = 5,7,9,1
# #基础解包（变量数量要和容器的元素数量一致）
a,b,c,d = t1
print(a,b,c,d)
# #扩展解包
x,*y,z = t1 #x为5，y为（7，9），z为1
s,*o = t1 #s为5，o为（7，9，1）
*o,e = t1 #s为（5，7，9），e为1
# #在元组解包时，*表示收集剩余所有的元素，允许我们处理不确定数量的元素（生成列表，以便于可以进行进一步的处理）

#案例，现有两个变量，分别为a = 10,b = 20,现需要将这两个变量值交换，然后输出到控制台
a = 10
b = 20
#组包
#t =b,a
#解包
#a,b = t
#合并
a,b = b,a
print(a)
print(b)
#案例2，现在有三个变量，分别为：a = 100,b = 200, c = 300,现需要将这个变量值进行交换,将a,b,c的值分别赋给c,a,b,并将其输出到控制台
a = 100
b = 200
c = 300
a,b,c = c,a,b
print(a)
print(b)
print(c)
#案例 根据提供的学生成绩单，完成如下需求
#1，计算每个学生的总分，各科平均分，然后一并输出出来。
#2，统计各科成绩的最高分，最低分，平均分，并输出
#3，查找成绩优秀（平均分大于90）的学生，并输出
students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周轶", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "遁天", 66, 59, 72)
)
#1，计算每个学生的总分，各科平均分，然后一并输出出来。------>{avg:.1f} 保留一位小数
print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
for s in students:
    total = s[2] + s[3] + s[4]
    avg = total / 3
    print(f"{s[0]}\t{s[1]} \t {s[2]} \t {s[3]} \t {s[4]} \t {total} \t {avg:.1f}")
#方式二
print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
for id,name,chinese,math,english in students:
    total = chinese + math + english
    avg = total / 3
    print(f"{id}\t{name} \t {chinese} \t {math} \t {english} \t {total} \t {avg:.1f}")





#2，统计各科成绩的最高分，最低分，平均分，并输出
#2.1获取各科成绩
chinese_scores = [s[2] for s in students]
math_scores = [s[3] for s in students]
english_scores = [s[4] for s in students]
print(f"语文的最低分{min(chinese_scores)},最高分{max(chinese_scores)},平均分{sum(chinese_scores)/len(chinese_scores)}",)
print(f"数学的最低分{min(math_scores)},最高分{max(math_scores)},平均分{sum(math_scores)/len(math_scores)}")
print(f"英语的最低分{min(english_scores)},最高分{max(english_scores)}，平均分{sum(english_scores)/len(english_scores)}")

#3，查找成绩优秀（平均分大于90）的学生，并输出
print("优秀学生名单如下：")
for s in students:
    total = s[2] + s[3] + s[4]
    avg = total / 3
    if avg > 90: #优秀学生
        print(f"学号:{s[0]},姓名{s[1]},平均分{avg:.1f}")