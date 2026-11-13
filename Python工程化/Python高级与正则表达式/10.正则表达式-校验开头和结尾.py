"""
^ 开头符
$ 结尾符
"""

#校验字符串必须要以数字开头，无论match(),还是search(),后边是什么无所谓
import re

from openai.types.admin.organization import group

result = re.match(r'^\d.*','1hm123')
print(result.group() if result else '匹配失败')
