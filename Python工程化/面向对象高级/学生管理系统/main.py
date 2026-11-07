"""
作为程序的入口文件
"""
from StudentCms import StudentCms
from Student类 import Student
#12.在main.py中测试
if __name__ == '__main__':
    #12.1创建学生管理系统对象
    cms = StudentCms()
    #12.2调用学生管理系统对象的start()函数，启动学生管理系统
    cms.start()