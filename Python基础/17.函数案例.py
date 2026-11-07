#案例1,定义一个函数，根据输入的底和高计算三角形面积的函数（三角形面积=底*高/2）
def sanjiao_area(d,h):
    area = d * h / 2
    return area
d = int(input("三角形底边长："))
h = int(input("三角形高："))
area = sanjiao_area(d,h)
print(area)

#案例2，定义一个函数，计算传入的一个字符串中元音字母的个数（元音字母为aeiouAEIOU）
def count_aeious(s):
    count = 0
    for i in s:
        if i in 'aeiouAEIOU':
            count += 1
    return count
print(count_aeious("hello"))

#案例3，定义一个函数，计算传入的高中学员成绩的最高分和最低分，平均分（保留一份小数），并返回
def calc_score():
    """
    计算传入的高中学员成绩的最高分和最低分，平均分
    :return:最高分和最低分，平均分
    """
    max_s = max(calc_score)
    min_s = min(calc_score)
    avg_s = round(sum(calc_score)/len(calc_score),1)
    return max_s, min_s, avg_s

s_list = [589,609,605,543,677,455,477,489,503]
calc_score(s_list)
max_s, min_s, avg_score = calc_score(s_list)
print(max_s, min_s, avg_score)