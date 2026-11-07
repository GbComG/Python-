#导入整个模块 ------>调用方式 模块名.功能名
# import random as rd
#
# for i in range(100):
#     print(rd.randint(1,100))
#导入模块中的功能  from...import...
from random import randint as rint
for i in range(100):
    print(rint(1, 100))
