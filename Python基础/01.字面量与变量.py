#字面量的写法
print(100)#整数（int)
print(3.14)#浮点数/小数(float)
print(True)#布尔(bool)
print(False)#布尔(bool)
print("Hello Python")#字符串(str)
print("-----------------")#字符串(str)
print(None)#空值(NoneType)

#布尔类型本质上也是整数类型(True-1;False-0)
print(True+1)#2
print(False-1)#-1

#s变量,python是动态类型语言，一个变量是可以储存不同类型的数据的（但是项目开发中，推荐变量只储存一种数据类型）
num = 1114.1
print(num)

num = num + 1
print(num)

num = "ok"
print(num)

num = True
print(num)
num = False
print(num)

#案例
base = 20.7 # 基础播放量
incr = 50 # 每一个月的新增播放量
print("未来第一个月的播放总量:", base + incr)
print("未来第二个月的播放总量:", base + incr+incr)
#案例-升级，一次性可以定义多个变量
base,incr = 20.7,50
print("未来一个月的播放总量；",base+incr)
print("未来第二个月的播放总量:", base + incr+ incr)
print("未来第二个月的播放总量:", base + incr*2)

#标识符
true = 1
print(true)

a = 10
b = 20
a,b = b,a
print(a)
print(b)

a=10
b=20
a = c = 10 #c = 10
a = b #a = 20
b=c#b = 10
print(a)
print(b)

a = 100;b = 200;c = 300
d = b#d=200
b = c #b = 300
c = a #c = 100
a = d #a = 200
print(a,b,c)





