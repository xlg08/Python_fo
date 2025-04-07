"""
    文件操作三步走：
        1.打开文件
        2.读写文件
        3.关闭文件

    1.打开文件：注意  在进行文件操作之前，一定要提前打开文件，否则无法对文件进行操作
        open()方法：用来打开一个文件
        原理：如果打开文件不存在，则自动创建一个新的文件
        格式：open("文件名","操作模式")
            文件名： 注意路径：绝对路径或者相对模式
            操作模式：
            r :  read,代表以只读的方式打开文件
            w :  write，代表以只写的方式打开文件  原理：首先要清空整个文件的内容，从头开始写入
            a :  append。代表以追加的方式打开文件，实现数据写入  原理：不需要清空文件的原有内容，在文件基础上进行追加操作
                -----以上r,w,a主要是针对文件文件进行操作
                -----以下对图形，音频，视频这些非文件文件进行操作
            rb :  binary ，以二进制的方式读取文件
            wb :  binarg ，以二进制的方式写入文件


"""

# 打开一个文件，并且向文件中追加一句话"社会主义好"
# 1.打开一个文件
# filename = open("python.txt", "a", encoding="utf-8")
# print(filename)
# # 2.对文件进行写操作
# list1 = []
# for i in range(1, 101):
#     list1.append(str(i))
# list1.append("\n")
# # filename.write(str(list1))      # write 方法 只能接受字符串参数
# filename.writelines(list1)      # writelines 方法
# # 3.关闭文件流，释放资源
# filename.close()


# 读取文件
# 1.打开文件
filename2 = open("python.txt", "r", encoding="utf-8")
# 2.读取文件
# read()   # 读取文件的所有内容
# read(1024)    # 读取1024个字符长度文件内容，字母或者数字
content = filename2.read()
print(content)


