

# True只等于1 ，False只等于0，
# print(3 == True)        # 此处为False

a = "a"
print(hex(id("a")))
print(hex(id(a)))
print(id(a))
a = "b"
print(hex(id("b")))
print(hex(id(a)))
print(id(a))

# 0x7ff907e3bce0    =>  140707555949792
# 0x7ff907e3c100    =>  140707555950848
print("♥"*30)
a = 1
print(hex(id(1)))
print(hex(id(a)))
print(id(a))
# a = 100000000000000000000000000000000000000000000000000000000000000
# print(hex(id(100000000000000000000000000000000000000000000000000000000000000)))
a = 10
print(hex(id(10)))
print(hex(id(a)))
print(id(a))



