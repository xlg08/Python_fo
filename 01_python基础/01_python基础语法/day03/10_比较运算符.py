import sys

a=4553223
b=a
c=[a]
c.append(a)
print(sys.getrefcount(a))