# """
#     __dict__ 属性介绍
#         python内置的，可以把对象转换为字典
#
# """
#
# from StudentManagerSystem.student import Student
#
# s1 = Student("周云杰", "男", 60, "554645", "海尔老总")
# s2 = Student("周云杰2", "男", 30, "554645", "海尔小总")
# s3 = Student("周云杰3", "男", 35, "554645", "海尔总总")
#
# stu_list = [s1, s2, s3]
# print(stu_list)
#
# # print(s1)
# # 转成字典 {'name': '周云杰', 'gender': '男', 'age': 60, 'phone': '554645', 'desc': '海尔老总'}
# # mydicts1 = s1.__dict__
# # print(mydicts1)
#
# # 列表推导式
# list_change_dict = [stu.__dict__ for stu in stu_list]
# print(list_change_dict)
#
# # 需求：字典转换为对象
# my_dict = {'name': '周云杰', 'gender': '男', 'age': 60, 'phone': '554645', 'desc': '海尔老总'}
# s6 = Student(**my_dict)
# print(s6)
# print(type(s6))

def oo():
    print("oo")