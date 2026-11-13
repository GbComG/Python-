"""
*   匹配前面的字符 0 次或多次
?   匹配前面的字符 0 次或 1 次
+   匹配前面的字符 1 次或多次
{n}   匹配前面的字符恰好 n 次
{n,}  匹配前面的字符至少 n 次
{n,m} 匹配前面的字符 n ~ m 次
"""

import re

#1  .*  .*匹配时，前边是啥无所谓，后边是啥也无所谓
result = re.match('.*hm.*','abchm123') #成功
#2  +
result = re.match('.+hm','abchm123') #成功
result = re.match('.+hm','hm123') #失败，因为至少要匹配前面一次
# .?
result = re.match('.?hm','ahm123') #成功
result = re.match('.?hm','hm123') #成功
result = re.match('.?hm','wzhm123') #失败
#{n}
result = re.match(r'\d{3}hm\w{2,5}','123hm123') #成功
print(result.group() if result else '未匹配')
