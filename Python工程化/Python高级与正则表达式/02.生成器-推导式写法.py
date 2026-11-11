"""
案例：演示生成器之 推导式写法

生成器介绍：
    概述：
        所谓的生成器就是基于 数据规则，用一部分生成一部分，而不是一下子生成完所有。
    目的：
        可以节省大量的内存。
    实现方式：
        1. 推导式写法。
        2. yield关键字
"""

import sys

#场景一:生成器推导式写法
#需求1:生成1-10之间的整数
my_generator = (i for i in range(1,11))
print(my_generator)
print(type(my_generator))
print('*'*30)
#需求2:生成1-10之间的偶数
my_gt2 = (i for i in range(1,11) if i % 2 == 0)
print(my_gt2)
print(type(my_gt2))
print('*'*30)
#需求三:如何从生成器中获取数据
#思路1:next()
print(next(my_gt2)) #2
print(next(my_gt2)) #4
print('*'*30)
for i in my_gt2:
    print(i)
# 6 8 10  因为next获取数据的底层可以理解为指针的移动，前两次取值已经令指针指向了4,所以再开始遍历，指针下移会从6开始遍历

my_list = [i for i in range(10000000)]
my_gt3 = (i for i in range(10000000))
print(type(my_list),type(my_gt3))
print(f'my_list的内存占用:{sys.getsizeof(my_list)}')
print(f'my_gt3的内存占用:{sys.getsizeof(my_gt3)}')
