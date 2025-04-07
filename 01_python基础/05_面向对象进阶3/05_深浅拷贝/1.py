import copy





j = [55,11]
b = [1, 2, 3, j]

c = copy.copy(b)
b[3][0] = 66


# print(id(c))
# print(id(b))
# print(id(c) == id(b))
#
# print(id(c[0]))
# print(id(b[0]))
# print(id(c[0]) == id(b[0]))
#
# b[0] = 9
#
# print(id(c[0]))
# print(id(b[0]))
# print(id(c[0]) == id(b[0]))
