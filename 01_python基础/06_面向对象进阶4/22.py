import copy

a = [1, 2, 3]
b = [10, 20, a]
b[0] = 30
b[2][0] = 4
print("拷贝前的b：", b)
# b = [30,20,[4,2,3]]
c = copy.copy(b)
b[0] = 10
b[2][0] = 55
print("拷贝后的b：", b)
print("拷贝后的c：", c)
