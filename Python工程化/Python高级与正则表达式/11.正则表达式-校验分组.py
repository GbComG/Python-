# |     或
# ()    分组
# \num  引用第 num 组
#
# 扩展：
# (?P<分组名>) 命名分组
# (?P=分组名) 引用命名分组

#需求:在列表fruits = ['apple','orange','pear']匹配apple和pear
import re
#1.定义水果列表
fruits = ['apple','orange','pear']
#2.遍历找到每种水果
for fruit in fruits:
    #判断当前水果是否是喜欢吃的水果
    if re.match(r'apple|pear',fruit):
        print(f'喜欢吃{fruit}')
    else:
        print(f'不喜欢吃{fruit}')
