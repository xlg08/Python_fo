"""
    字符串修改：通过函数(方法)的形式修改字符串中的数据

    replace(): 返回替换后的字符串
    split():   返回切割后的列表序列
    title():   所有单词首字母大写

"""

str1 = "hello python hello linux hello Windows"

# 要替换的内容，替换后的内容，替换的次数
str1.replace("hello", "Hello")           # 默认有几个替换几个
str1.replace("hello", "Hello", 1)         # 指定替换个数

# split
list1 = str1.split(" ")
print(list1)

# join()方法： 和split()方法正好相反，其主要功能是把序列拼接为字符串
# 字符串.join(数据序列)

str3 = " ".join(list1)
print(str3)

str4 = str1.title()
print(str4)










