"""
    集合
        概念：天生的去重的无序的数据集合  (数据容器)
    基本语法：
        格式一：集合名称 = {具体的数据}
        格式二：集合名称 = set(具体的数据)
        注意格式一集合里面传  集合名称 = {具体的数据}  key value


"""

set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2}

# 集合天然去重
# print(set1)  # 2被去掉了
#
# set2 = {"a", "b", "c", "d", "e"}
# print(set2)

# stu = set()
# stu.add("李哲")
# stu.add("刘毅")
# stu.add("李雷")
# stu.add("韩梅梅")
# print(stu)

# remove() 方法：删除集合中的指定数据，如果数据不存在则报错。

# studnts = {1, 2, 3, 4, 5, 6, (1,25)}
# a = set()
# a = studnts.copy()      #
# print(id(studnts))
# studnts.clear()     # 清除集合中的元素
# print(id(a))
# print(id(studnts))
# print(studnts)
# print(a)

# original = { (1, [2, 3]) }
# copy_set = original.copy()
#
# # 获取原集合中的元组（注意：集合无序，需通过迭代获取）
# elem_original = next(iter(original))
# print(elem_original)
# # 修改元组内的列表
# elem_original[1].append(4)
#
# print(original)  # 输出：{(1, [2, 3, 4])}
# print(copy_set)   # 输出：{(1, [2, 3, 4])}（与原集合同步变化）
import gc

a, b, c, d = "a", "b", "c", "d"
e = a + b
# set_1 = {a, b, c, d, e}
for i in range(10):
    set_1 = {a, b, c, d, e}
    print(f"a:{hash(a)}\tb:{hash(b)}\tc:{hash(c)}\td:{hash(d)}\te:{hash(e)}")
    # print(f"a:{id(a)}\tb:{id(b)}\tc:{id(c)}\td:{id(d)}\te:{id(e)}")
    print(set_1)
    for z in set_1:
        del z
    # del set_1
    # del e
    # gc.collect()
print(set_1)
print(set_1)


