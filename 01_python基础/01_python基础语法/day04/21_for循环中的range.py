"""
    range 方法 主要作用是用来生成一个容器对象 range(5) ->
                                存储了5个对象：0  1  2  3  4

    其内部方法一般是一个数字，代表指定长度的数据容器
    元素特点：顾头不顾尾(左闭右开)  元素 ：0~4  长度 ：5

    完整格式：
        range(start, stop,[step])       # 默认从0开始,步长默认为1
        start:开始
        stop：结束     #
        step：步长

"""
# for temp in range(5):
#     print(temp, end="\t")
#
# print()
# for temp in range(0, 5, 1):     # [0,5)
#     print(temp, end="\t")
#
# print()
# for temp in range(0, 5, 6):
#     print(temp, end="\t")
#
# print()
# for temp in range(-19, -3, 1):
#     print(temp, end="\t")
#
# print()
for temp in range(-1, -13, -1):
    print(temp, end="\t")

