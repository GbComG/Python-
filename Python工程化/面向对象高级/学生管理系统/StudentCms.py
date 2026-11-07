"""
该文件用于完成学生管理系统的具体业务,即：增删查改，保存学生信息等
"""
from shutil import which

#导包
from Student类 import Student
import time
#1.创建学生管理系统类:
class StudentCms(object):
    #2.通过魔法方法__init__,初始化属性信息
    def __init__(self):
        #创建一个空壳，用于存储学生信息
        self.stu_list = [] #[学生对象，学生对象，学生对象...]->[Student(),Student(),Student()...]
    #3.定义一个函数打印开始界面
    def show_view(self):
        print('*' * 23)
        print("""本学员管理系统V2.0可完成如下操作：
    \t1.添加学员;
    \t2.修改学员;
    \t3.删除学员;
    \t4.查询某个学员;
    \t5.显示所有学员;
    \t6.保存信息;
    \t0.退出系统;""")
        print('*' * 23)
        print()

    #4.定义函数，实现添加学生信息功能;
    def add_student(self):
        name = input("请输入学生姓名:")
        gender = input("请输入学生性别:")
        age = int(input("请输入学生年龄:"))
        phone = input("请输入学生电话:")
        desc = input("请输入学生描述信息:")
        stu = Student(name, gender, age, phone, desc)
        self.stu_list.append(stu)
        print(f'添加{name}学生信息成功!\n')
    #5.定义函数，实现删除学生信息功能;
    def delete_student(self):
        pass
    #6.定义函数，实现修改学生信息的功能;
    def update_student(self):
        pass
    #7.定义函数，实现查找单个学生信息功能;
    def search_one_student(self):
        pass
    #8.定义函数，实现查找全部学生信息功能;
    def search_all_student(self):
        #8.1 判断长度是否为零
        if len(self.stu_list) == 0:
            print("当前系统内并未存有学生信息.")
        #8.2 长度不为零，遍历列表打印所有信息
        else:
            for stu in self.stu_list:
                print(stu)
            print()
    #9.定义函数，实现保存学生信息功能;
    def save_student(self):
        #9.1 关联 学生信息文件
        with open('./面向对象高级/学生管理系统/stu.txt','w',encoding='utf-8') as dest_f:
            #9.2 把[学生对象。学生对象，学生对象]-->[字典，字典，字典]
            stu_dict = [stu.__dict__ for stu in self.stu_list]
            #9.3 把字典列表持久化到文件中
            dest_f.write(str(stu_dict))
            print('保存成功!\n')
    #10.定义函数，实现加载学生信息;
    def load_student(self):
        #10.1：加入异常处理，有可能文件不存在
        try:
            #10.2 关联学生信息文件
            with open('./面向对象高级/学生管理系统/stu.txt','r',encoding='utf-8') as src_f:
            #10.3 一次性读取所有数据
                stu_data = src_f.read()
            #10.4 把上述字符串转换为列表.
                stu_list = eval(stu_data)
            #10.5 判断若列表长度为0，赋予其空列表
                if len(stu_list) == 0:
                    stu_list = []
            #10.6 把stu_list（列表套字典）转换为[学生对象,学生对象...]
                self.stu_list = [Student(**stu_dict) for stu_dict in stu_list]
        except FileNotFoundError: #提示没有文件，创建即可
            with open('./面向对象高级/学生管理系统/stu.txt','w',encoding='utf-8') as src_f:
                pass
    #11.定义函数，把上述的所有业务逻辑跑通.
    def start(self):
        #11.1 加载学生信息
        StudentCms.load_student()
        #11.2 循环
        while True:
            #11.3 打印学生管理系统界面 为了效果更明显，加入延迟（休眠线程）
            time.sleep(1)
            self.show_view()
            #11.4 提示用户输入数字选择自己要使用的功能
            input_num = int(input('请输入您要使用的功能编号:'))
            match input_num:
                case 1:
                    print('添加学生信息')
                    self.add_student()
                case 2:
                    print('修改学生信息')
                    self.update_student()
                case 3:
                    print('删除学生信息')
                    self.delete_student()

                case 4:
                    print('查找单个学生信息')
                    self.search_one_student()
                case 5:
                    print('查找全部学生信息')
                    self.search_all_student()
                case 6:
                    print('保存学生信息')
                    self.save_student()
                case 0:
                    #退出系统前确定是否需要保存学生信息
                    choice=input("请再次确认是否退出系统(Yes or No):")
                    if choice=='Yes':
                        save = input('是否要保存本次更改?(Yes or No):')
                        if save=='Yes':
                            StudentCms.save_student()
                        print('感谢您的使用，期待下次相见')
                        break
                    elif choice=='No':
                        continue
                    else:
                        print("错误，请输入Yes or No.")
                case _:
                    print('录入有误，请重新录入!')
                    continue





