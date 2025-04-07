
str = "abcde"
print("1：", str)
print("2：", str[0:3:-1])
print("3：", str[-1:-3:1])
print("4：", str[-1:3:1])
print("5：", str[1:-3:1])      # b
print("6：", str[-1:3:-1])     # e
print("7：", str[3:-1:-1])
print("8：", str[3:-3:1])
print("9：", str[3:-2:-1])
print("10：", str[-3:1:1])

# 起始序列默认是 0 或者是 -1 具体是几，要看步长
# str = "abcde"
print("11", str[::-1])
print("12", str[0::-2])     # a
print("13", str[-1::1])     # e
print("14", str[-1::2])     # e
# print("15", str[::0])   # 报错 步长不能为0
# print("16", str[::0.5])   # 报错 步长要为整数