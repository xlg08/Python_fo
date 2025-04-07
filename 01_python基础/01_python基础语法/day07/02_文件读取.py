"""
    # 读取文件的所有内容
        read()      相当于linux命令中的cat

    # 读取1024个字符长度文件内容，字母或者数字
    # 设置读取长度
        read(1024)  相当于linux命令中的

    readline()方法：       # 和循环搭配使用
        一次读取一行内容，每运行一次readline()函数，其就会将文件的指针向下移动一行

    readlines()方法：主要用于文本类型数据的读取
        readlines可以按照行的方式把整个文件中的内容进行一次性读取，
        并且返回的是一个列表，其中每一行的数据为一个元素。


"""

# # 读取文件
# # 1.打开文件
# filename1 = open("python.txt","r",encoding="utf-8")
# # 2.读取文件
# content = filename1.read()
# print(content)


filename2 = open("data.txt", "r", encoding="utf-8")

# c = filename2.readlines(10)     # 按照行的方式进行读取，返回一个列表
# print(c)

while True:
    tf = filename2.readline()   # 一次读取一行，读完指针下移
    if not tf:
        print("\n现在是：",type(tf))
        print(not "")
        break
    print(tf, end="")
filename2.close()


