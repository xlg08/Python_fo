a = 0
b = 1


if a > b:
    maxNum = a
else:
    maxNum = b
# 等价于
maxNum = a if a > b else b
'''
    exp1   if  condition   else   exp2
    表达式1 if    判断条件    else   表达式2
    
    condition 是判断条件，exp1 和 exp2 是两个表达式。
    如果 condition 成立（结果为真），
        就执行 exp1(表达式1)，并把 exp1 的结果作为整个表达式的结果；
    如果 condition 不成立（结果为假），
        就执行 exp2(表达式2)，并把 exp2 的结果作为整个表达式的结果。

    实例：max = a if a>b else b的含义是：
        如果 a>b 成立，
            就把 a 作为整个表达式的值，并赋给变量 max；
        如果 a>b 不成立，
            就把 b 作为整个表达式的值，并赋给变量 max。

'''

# 三目运算符的嵌套
'''
    Python 三目运算符支持嵌套，如此可以构成更加复杂的表达式。
        但是在嵌套时需要注意 if 和 else 的配对，
    例如：
        a if a>b else c if c>d else d
        等价于
        a if a>b else ( c if c>d else d )
'''
"""
实例:判断两个数字的关系：
"""
a = int(input("Input a: "))
b = int(input("Input b: "))

print("a大于b") if a > b else print("a小于b") if a < b else print("a等于b")
print("a大于b") if a > b else (print("a小于b") if a < b else print("a等于b"))
"""
    可能的运行结果：
        Input   a: 45
        Input   b: 100
        a小于b
"""

"""
    先对 a>b 求值
        如果该表达式为 True，程序就返回执行第一个表达式 print(“a大于b”)，
        否则将继续执行 else 后面的内容，
            也就是：( print("a小于b") if a<b else print("a等于b") )
            进入该表达式后，先判断 a<b 是否成立，
                如果 a<b 的结果为 True，将执行 print(“a小于b”)，
                否则执行 print(“a等于b”)    
"""
