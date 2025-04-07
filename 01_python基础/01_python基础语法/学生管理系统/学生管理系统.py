import fileOs
import os
"""
    数据该用什么容器进行存储
    学生信息  姓名、年龄、班级

    列表 + 字典

"""

students = []

# 添加学生
def add_student():

    # 接受学生信息
    name = input("请输入您的姓名：\n")
    age = input("请输入您的年龄：\n")
    class_num = input("请输入您的班级：\n")

    # 创建字典  （数据已经来了，考虑存放容器）
    student = {}
    student["name"] = name
    student["age"] = age
    student["class_num"] = class_num

    # students = []
    students.append(student)
    # print("add_student")
    # fileIO.addStudentToFile(students)      # 将信息添加到文件

    print(f"学生{name}信息添加成功！")


# 删除学生
def del_student():
    name = input("请输入您想删除学生姓名：\n")
    for i in students:
        if i["name"] == name:
            students.remove(i)
            print(f"{name}学生删除成功")
            break
    else:
        print(f"您要删除的{name}信息不存在")



# 修改学生信息
def edit_student():
    old_name = input("请输入您想修改的学生姓名：\n")
    for i in students:
        if i['name'] == old_name:
            i['name'] = input("请输入新名字：\n")
            i['age'] = input("请输入新年龄：\n")
            i['class'] = input("请输入新班级：\n")
            print("学生信息修改成功！")
            break
    else:
        print("您要修改的学生的姓名不存在")

    print("edit_student")


# 查询学生信息
def get_student():
    name = input("请输入您要查询学生姓名：\n")
    for i in students:
        if i["name"] == name:
            print(f"查询到学生姓名：{i['name']}，年龄：{i['age']}，班级：{i['class_num']}")
            break
    else:
        print(f"您要查询的{name}学生不存在")



# 遍历学生信息
def get_all_student():
    students.extend(fileOs.getStudents())
    for i in students:
        print(i)


# 退出系统
def get_out_student():
    os._exit(0)

def save_students():
    print(students)
    fileOs.addStudentToFile(students)


# 定义菜单函数
def menu():
    print("*" * 35)
    print("欢迎登录学生管理系统")
    print("1:添加学生信息")
    print("2:删除学生信息")
    print("3:修改学生信息")
    print("4:查询学生信息")
    print("5:遍历所有学生信息")
    print("6:保存学生信息")
    print("7:退出系统")


while True:
    menu()
    user_num = int(input("请输入您要选择的功能"))
    if user_num == 1:
        add_student()
    elif user_num == 2:
        del_student()
    elif user_num == 3:
        edit_student()
    elif user_num == 4:
        get_student()
    elif user_num == 5:
        get_all_student()
    elif user_num == 6:
        save_students()
    elif user_num == 7:
        get_out_student()



