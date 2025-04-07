"""
    二分（折半）查找
        概述：
            属于查找类的算法，相对来说效率比较高。时间复杂度 O(logn)
        前提：
            列表必须有序
        原理：
            1.比较 要查找的元素和列表中的值，如果一样则返回True。程序结束
            2.如果 要查找的元素比中值小，去前半段（中值前）查找
            3.如果 要查找的元素比中值大，去后半段（中值后）查找
            4.重复上述动作，直至找完。如果找完了，还没找到。就返回False
"""

# my_list 原列表 target 要查找的目标值
def binary_search_re(my_list, target):
    # 获取列表长度
    n = len(my_list)
    # 判断列表是否为空
    if n == 0:
        return False
    mid = n//2
    # 比较 要查找的元素 和 中值
    if my_list[mid] == target:
        return True
    elif target < my_list[mid]:
        # 如果要查找的元素 比中值小 ， 去前半段（中值前查找）。递归调用
        # [:mid] 采用切片，包左不包右
        return binary_search_re(my_list[:mid], target)
    else:
        return binary_search_re(my_list[mid+1:], target)

    # return False

if __name__ == '__main__':
    my_list = [2, 3, 4, 5, 6]
    print(binary_search_re(my_list, 4))

