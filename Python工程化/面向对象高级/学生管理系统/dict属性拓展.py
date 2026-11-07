"""
演示python内置的dict属性
    __dict__属性介绍:
        这是python内置的属性，可以把对象转换成字典形式.
"""
from Python工程化.面向对象高级.学生管理系统.Student类 import Student
#需求1.把学生对象转化成字典属性
s1 = Student('王瑶',18,'女',2391539245,'校花')
print(s1)

my_dict = s1.__dict__
print(my_dict)
print(type(my_dict))
print('*'*20)

#需求2.把[学生对象。学生对象，学生对象]-->[字典，字典，字典]
s1 = Student('张宏瑞',18,'女',2391539245,'校花') #她让我改成她的名字，本来不想写她的
s2 = Student('王子煊',18,'男',15532291853,'校草')
s3 = Student('大迫杰',35,'男',12345678900,'王子煊本人')
student_list = [s1,s2,s3]
#列表推导式
list_tuple = [stu.__dict__ for stu in student_list]
print(*list_tuple,sep="\n")
#需求3.把 {'name': '王子煊', 'age': 18, 'sex': '男', 'phone': 15532291853, 'desc': '校草'}  --> 学生对象

    #方法1.
my_dict = {'name': '王子煊', 'age': 18, 'sex': '男', 'phone': 15532291853, 'desc': '校草'}
s5 = Student(my_dict['name'],my_dict['age'],my_dict['sex'],my_dict['phone'],my_dict['desc'])
print(s5)

    #方法二
s5 = Student(**my_dict)
print(s5)