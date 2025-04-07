import os

"""

    文件操作相关方法
        os.rename(旧文件名称，新文件名称)：对文件进行重命名操作 |
        os.remove(要删除文件名称)     ：  对文件进行删除操作

    文件夹操作：
        os.mkdir(新文件夹名称)
        os.getcwd()
        os.chdir(切换后目录名称)
        os.listdir(目标目录)
        os.rmdir(目标目录)
        
    ### 文件夹删除补充（递归删除、慎重！）
    
        # 导入shutil模块
        import shutil
        # 递归删除非空目录
        shutil.rmtree('要删除文件夹路径')
        
        递归删除文件夹的原理：
            理论上，其在删除过程中，如果文件夹非空，则自动切换到文件夹的内部，然后把其内部的文件，
                一个一个删除，当所有文件删除完毕后，返回到上一级目录，删除文件夹本身。

"""
print("♥"*50)
# os.mkdir("haha")
print(os.getcwd())
# os.mkdir("lala")
print(os.chdir("../"))
print(os.listdir())
print(os.chdir("./day07"))
print(os.rmdir("./lala"))