import sys

num = [10,20,30]
# print(id(num[0]))
# print(id(num[1]))
# print(id(num[2]))
# print(id(10))
# print(id(11))
# print(num.__sizeof__())
# print(num[0].__sizeof__())
print(sys.getsizeof(id(num[0])))
print(sys.getsizeof(id(10)))


