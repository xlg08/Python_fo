def my_fun():
    for i in range(1, 11):
        # yield i 再次做了三件事
        #   1. 创建生成器对象
        #   2.把值存储到生成器中
        #   3.返回生成器
        yield i

        # 等价于
        # my_list = []    # 1.创建
        # for i in range(1, 11):      # 2.添加
        #     my_list.append(i)
        # return my_list          # 3.返回

# 1.创建生成器对象
my_g1 = my_fun()
print(type(my_g1))      #
print(next(my_g1))
print(next(my_g1))

print("*" * 30)

for i in my_g1:
    print(i)