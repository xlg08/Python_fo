from typing import final
import mypy
from beartype import beartype


'''
    在 Python 的 typing 模块中，
    @final 装饰器用于指示一个方法（或类）不应该被子类覆盖（override）。
'''
# class B:
#
#     def __init__(self):
#         pass
#
#     @final
#     def aa(self, a: int) -> None:
#         print(a)


class A(object):
    @beartype
    def aa(self, a: 'A') -> None:
        print(a)


class B(A):

    def aa(self, a: 'A') -> None:
        print(a)

class C():
    def aa(self, a: 'A') -> None:
        print(a)

if __name__ == '__main__':
    a = A()
    a.aa(a)

    b = B()
    a.aa(b)

    b: A = B()
    a.aa(b)

    c: C = C()
    a.aa(c)
