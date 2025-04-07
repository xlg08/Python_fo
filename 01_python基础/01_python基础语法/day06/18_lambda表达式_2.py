# 如何修改lambda表达式
funb = lambda : 10
print(funb)         # <function <lambda> at 0x000001D43D0AE520>
print(funb())   # 10

print((lambda  : 10)())

# 特别注意：由于lambda表达式没有名字，所以在实际的工作中必须把他赋值给某一个变量，否则无法直接调用
