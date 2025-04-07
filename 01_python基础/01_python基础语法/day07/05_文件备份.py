"""
    需求分析：
        拷贝文件并改名
        例如：把 a.txt 文件  拷贝到 a[备份].txt 文件中

    分析：
        1.用户输入要备份的文件名称
            字符串：a.txt  -->  a[备份].txt
        2.

"""


filename1 = input("输入：")

# 第二步：拆  rfind 从右找起，返回找到的第一个的索引位置
index = filename1.rfind(".")    # "."出现索引的位置   a.txt    0  1  2  3  4

print(index)            # "."出现索引的位置   a.txt    0  1  2  3  4

if index > 0:
    # 用户输入的文件名
    old_name = filename1[:index]    # print(old_name)
    # 用户输入后缀
    old_suffix = filename1[index:]
    # 拼接新文件的名字
    new_name = old_name + "[备份]" +old_suffix

    # 读写文件
    old_f = open(filename1,"r",encoding="utf-8")
    new_f = open(new_name,"w",encoding="utf-8")

    while True:
        c = old_f.read()
        if len(c) == 0:
            break
        new_f.write(c)
    old_f.close()
    new_f.close()
else:
    print("请正确输入文件名如：python.txt")
