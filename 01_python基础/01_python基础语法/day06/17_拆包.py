# """
#     拆包：
#         就是把一个元组中的数据一个一个拆解出来的过程
#
# """
# tuple1 = (10, 20)
# for e in tuple1:
#     print(e)
#
# # 不需要使用for循环，拆包即可
# # 拆包
# num1, num2 = tuple1
# print(num1)
# print(num2)
#
# # 没给够，将元组直接复制给变量
# num1 = tuple1
#
# tuple1 = (10, 20, 30)
# num1, num2 = tuple1
# print("------", num1, num2)
#
# # 给多了，会报错报错
# num1, num2, num3 = tuple1
#
# # 等价于
# num1, num2 = (10, 20)
# num1, num2 = 10, 20


