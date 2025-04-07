"""
    该类的作用就是完成学生管理的操作 ： 即 增删改查

"""
import os

from student import Student

class StudentCMS:

    def __init__(self):
        self.stu_list = []

    # 实现功能（定义方法）
    @staticmethod
    def show_view():
        print("*" * 24)
        print("学生管理系统V2.0面向对象版本")
        print("1:添加学生信息")
        print("2:删除学生信息")
        print("3:修改学生信息")
        print("4:查询某个学生信息")
        print("5:显示所有学生信息")
        print("6:保存学生信息")
        print("7:加载学生信息")
        print("0:退出系统")
        print("*" * 24)

    def add_student(self):
        name = input("请输入学生姓名：\n")
        gender = input("请输入学生性别：\n")
        age = input("请输入学生年龄：\n")
        phone = input("请输入学生电话：\n")
        desc = input("请输入学生描述：\n")
        stu = Student(name, gender, age, phone, desc)
        self.stu_list.append(stu)
        print(f"添加{name}学生信息成功")

    def update_student(self):
        upd_name = input("请输入要修改的学生的姓名：\n")
        for stu in self.stu_list:
            if stu.name == upd_name:
                stu.gender = input("请输入您要修改的性别：\n")
                stu.age = input("请输入您要修改的年龄：\n")
                stu.phone = input("请输入您要修改的电话：\n")
                stu.desc = input("请输入您要修改的描述：\n")
                print(f"学生{upd_name}信息修改成功")
        else:
            print("查无此人")

    def del_student(self):
        del_name = input("请输入你要删除学生的姓名：\n")
        for stu in self.stu_list:
            if stu.name == del_name:
                self.stu_list.remove(stu)
                print(f"学员{del_name}信息删除成功")
                break
        else:
            print("查无此人")

    def search_one_student(self):
        search_name = input("请输入您要查找学生的姓名：\n")
        for stu in self.stu_list:
            if stu.name == search_name:
                print(stu)
                break
        else:
            print("查无此人")

    def search_all_student(self):
        if len(self.stu_list) == 0:
            print("暂无学生信息")
        else:
            for stu in self.stu_list:
                print(stu)

    def save_student(self):
        with open("stu_data.txt", "w", encoding="utf-8") as dets_f:
            # 方法一
            # for stu in self.stu_list:
            #     dets_f.write(str(stu))

            # 方法二
            stu_dict = [stu.__dict__ for stu in self.stu_list]
            for stu in stu_dict:
                dets_f.write(str(stu))

    def exit_student(self):
        os._exit(0)

    # 加载 .txt 文本文件中的学生信息
    # 读文件
    # 遍历将文件内容加载列表中
    def load_student(self):
        try:   # 万一没有文件
            with open("stu_data.txt", "r", encoding="utf-8") as src_f:
                stu_data = src_f.read()     # [字典, 字典, 字典, ...]
                # 把里面的字符串，根据字符串的特点，推断合适的格式
                stu_list = eval(stu_data)
                if len(stu_list) == 0:
                        stu_list = []
                # for stu_dict in stu_list:
                # 把列表套字典转换为 [学生对象,学生对象,学生对象...] 赋值 self.stu_list
                self.stu_list = [Student(**stu_dict) for stu_dict in stu_list]
        except:
            with open("stu_data.txt", "w", encoding="utf-8") as src_f:
                pass
    def start(self):
        while True:
            StudentCMS.show_view()
            input_num = input("请您输入要操作的编号：\n")

            if input_num == "1":
                self.add_student()
            elif input_num == "2":
                self.update_student()
            elif input_num == "3":
                self.del_student()
            elif input_num == "4":
                self.search_one_student()
            elif input_num == "5":
                self.search_all_student()
            elif input_num == "6":
                self.save_student()
            elif input_num == "7":
                self.load_student()
            elif input_num == "0":
                self.exit_student()
            else:
                print("您输入的有误！！！")


if __name__ == '__main__':
    cms = StudentCMS()
    cms.start()
