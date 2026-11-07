#
print("Hello")
print(type("Hello"))
print(10)
print(type(10))
print(3.14)
print(type(3.14))
print(True)
print(type(True))
print(None)
print(type(None))

#常见数据类型-----isinstance(数据，类型)---布尔值---判定数据是否为指定的值
num = 3.14
print(isinstance(num,float))#True
print(isinstance(num,int))#False

#字符串
#字符串的三种定义方式
s1 = "Hello" #双引号定义
s2 = 'python' #单引号定义(两者都不能跨行)
s3 = """
1949年新中国成立
标志着三座大山被彻底推翻
人民当家作主的时代到来了
""" #三引号定义(可跨行)
print(s1)
print(s2)
print(s3)
print(type(s1))
print(type(s2))
print(type(s3))
#定义字符串------It'very good.
msg1 = 'It\'s very good.'
msg2 = "Hello 的意思就是\"你好\""
print(msg1)
print(msg2)
msg3 = "\t1949年新中国成立标志着三座大山被推翻\n\t人民当家作主的时代到来了"#\t代表缩进,\n代表换行
print(msg3)

#字符串的拼接
s1 = "人生苦短""我用python"",ok"
print(s1)
msg1 = "人生苦短"
msg2 = "我用python"
print("龟叔说："+ msg1+","+msg2)
#案例 str(int)将int转化为str
time = "两年半"
name = "个人练习生蔡徐坤"
hobby = "唱跳、rap、篮球。”"
print('各位全民制作人们大家好：“我是练习时长' + time + "的" + name + ",""喜欢"+hobby)

#字符串格式化 方式一：%s占位符
s1 = "人生苦短"
s2 = "我用python"
print("龟叔说：%s,%s."%(s1,s2))
name = "王子煊"
age = 17
hobby = ("跑步")
print("大家好，我是%s,今年%s，喜欢%s。"%(name,age,hobby))
name = "王子煊"
age = 17
hobby = "跑步"
print(f"大家好，我是{name},今年{age},我的爱好是{hobby}")


