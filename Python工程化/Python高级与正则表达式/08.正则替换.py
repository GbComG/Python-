"""
案例:演示正则替换
回顾正则的使用步骤：
1. 导包
import re

2. 创建匹配
result = re.match('正则表达式', '要校验的字符串')   # 从前往后依次匹配，只要前面匹配即可
result = re.search('正则表达式', '要校验的字符串')   # 分段查找
result = re.compile('正则表达式').sub(替换后的内容, 要被替换的字符串)  # 替换

3. 获取匹配结果
result.group()

"""
#导包
import re

#1.定义字符串
s= "开心你就大声笑，哈哈，呵呵，嘿嘿，咯咯，桀桀桀"
#2.把上述的 哈 呵  嘿 咯 桀 替换为 ❤️

#                       正则规则       新字符串   需要替换的字符串
result = re.compile('哈|呵|嘿|咯|桀').sub('❤️', s)
print(result)
print('--'*10)

result = re.sub('哈|呵|嘿|咯|桀','❤️', s)
print(result)