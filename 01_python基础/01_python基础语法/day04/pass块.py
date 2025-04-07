"""
    pass 是空语句，是为了保持程序结构的完整性。
    pass 不做任何事情，一般用做占位语句
    。
"""

# 输出 Python 的每个字母
for letter in 'Python':
    if letter == 'h':
        pass
        print('这是 pass 块')
    print('当前字母 :', letter)
print("Good bye!")

"""
    pass：一般用于占位置。
        例如：在 Python 中有时候会看到一个 def 函数:
        def sample(n_samples):
            pass
        该处的 pass 便是占据一个位置，因为如果定义一个空函数程序会报错，
            当没有想好函数的内容是可以用 pass 填充，使程序可以正常运行。
"""

"""
    python2.x：
        def function():
            # 空函数在Python2.x版本中pass是必须的
            pass
    python3.x
        def function():
            # 在Python3.x的时候pass可以写或不写
            pass
"""


