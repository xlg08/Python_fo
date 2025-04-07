"""
    字典的查询方法：
        使用具体的某个Key查询数据，如果未找到，则直接报错
        字典序列[Key]

    keys()  :  以列表返回一个字典的所有键
    values() : 以列表返回一个字典的所有值
    items()  : 以列表返回可遍历的(键，值)元组数据

    在python中，
        通过 keys方法来获取字典中所有的键
        通过 values方法来获取字典中所有的值

    基本语法：
        字典名称.keys()     返回的是以列表的形式
        字典名称。values()   返回的是以列表的形式

    提示：返回的都是列表


"""

d1 = {"name": "张三", "age": 18, "sale": "男"}

for k,v in d1.items():
    print(k,"\t",v)

# print(d1.keys())
# print(d1.values())
#
# # for temp in d1.keys():
# # 等价于
# for temp in d1:         # 遍历字典就是遍历字典的所有的键
#     if temp == "age":
#         d1[temp] = 15
#
# print(d1)







